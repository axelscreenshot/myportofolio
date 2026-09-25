import os
import sys
import django
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

USER_PASSWORD = os.getenv("E2E_USER_PASSWORD")
EDITOR_PASSWORD = os.getenv("E2E_EDITOR_PASSWORD")
ADMIN_PASSWORD = os.getenv("E2E_ADMIN_PASSWORD")

if not USER_PASSWORD or not EDITOR_PASSWORD or not ADMIN_PASSWORD:
    sys.exit("E2E_USER_PASSWORD, E2E_EDITOR_PASSWORD, E2E_ADMIN_PASSWORD belum diisi di berkas .env.")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portofolio.settings")
django.setup()
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from main.models import Project


def setup_editor_group():
    editor_group, created = Group.objects.get_or_create(name="Editor")
    
    if created:
        content_type = ContentType.objects.get_for_model(Project)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=["update_project"]
        )
        editor_group.permissions.set(permissions)

    return editor_group

def setup_test_project():
    project, _ = Project.objects.get_or_create(
        title="Test E2E Project",
        description="Test E2E Project Desc",
    )
    return project

def setup_users():
    # reg user
    user, _ = User.objects.get_or_create(username="burhan_test")
    user.set_password(USER_PASSWORD)
    user.is_superuser = False
    user.is_staff = False
    user.save()

    # editor user
    editor, _ = User.objects.get_or_create(username="editor_test")
    editor.set_password(EDITOR_PASSWORD)
    editor.is_superuser = False
    editor.is_staff = False
    editor.save()

    editor_group = setup_editor_group()
    editor.groups.add(editor_group)

    # super user
    admin, _ = User.objects.get_or_create(username="admin_test")
    admin.set_password(ADMIN_PASSWORD)
    admin.is_superuser = True
    admin.is_staff = True
    admin.save()


def main():
    setup_users()

    options = webdriver.ChromeOptions()
    if "--headless" in sys.argv:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    else:
        options.add_argument("--start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 10)
    base_url = "http://127.0.0.1:8000"

    try:
        # 1. Cek csrf token di form login
        try:
            driver.get(f"{base_url}/login/")
        except Exception:
            print(f"Server belum berjalan di {base_url}. Jalankan 'python manage.py runserver' terlebih dahulu.")
            return
        csrf = wait.until(
            EC.presence_of_element_located((By.NAME, "csrfmiddlewaretoken"))
        )
        assert csrf.get_attribute("value")
        assert driver.get_cookie("csrftoken")
        print("[PASS] CSRF token dan cookie terverifikasi")

        # 2. Cek login user biasa dan cookie sesi
        driver.find_element(By.NAME, "username").send_keys("burhan_test")
        driver.find_element(By.NAME, "password").send_keys(USER_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        wait.until(EC.url_to_be(f"{base_url}/"))
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "nav-user")))
        assert driver.get_cookie("sessionid")
        assert driver.get_cookie("last_login")
        assert "Sesi Terakhir Login" in driver.page_source or "Last Login" in driver.page_source
        print("[PASS] Login user biasa dan cookie sesi berhasil")

        # 3. Cek pembatasan akses user biasa ke form tambah proyek
        driver.get(f"{base_url}/projects/add/")
        assert "403" in driver.title or "Forbidden" in driver.page_source
        print("[PASS] Otorisasi user biasa dibatasi (403)")

        # 4. Cek pembatasan akses user editor ke form tambah proyek, akses editor ke form update proyek
        driver.get(f"{base_url}/logout/")
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/login/')]")))
        driver.get(f"{base_url}/login/")
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("editor_test")
        driver.find_element(By.NAME, "password").send_keys(EDITOR_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        wait.until(EC.url_to_be(f"{base_url}/"))
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "nav-user"), "editor_test"))

        driver.get(f"{base_url}/projects/add/")
        assert "403" in driver.title or "Forbidden" in driver.page_source
        print("[PASS] Otorisasi user editor dibatasi dari form add (403)")

        project = setup_test_project()
        driver.get(f"{base_url}/projects/{project.id}/update/")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "goods-form")))
        print("[PASS] Akses editor ke form update berhasil")

        # 5. Cek akses superuser ke form tambah proyek
        driver.get(f"{base_url}/logout/")
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/login/')]")))
        driver.get(f"{base_url}/login/")
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("admin_test")
        driver.find_element(By.NAME, "password").send_keys(ADMIN_PASSWORD)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        wait.until(EC.url_to_be(f"{base_url}/"))
        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "nav-user"), "admin_test"))

        driver.get(f"{base_url}/projects/add/")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "goods-form")))
        print("[PASS] Akses superuser ke form proyek berhasil")

        # 6. Cek logout dan penghapusan cookie
        driver.get(f"{base_url}/logout/")
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/login/')]")))
        cookie_last_login = driver.get_cookie("last_login")
        assert cookie_last_login is None or cookie_last_login["value"] == ""
        print("[PASS] Logout dan pembersihan cookie berhasil")

        print("\nSemua pengujian E2E berhasil!")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
