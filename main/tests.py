from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Project


class MainTest(TestCase):
    # setUp
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )

        self.project = Project.objects.create(
            title="This Website",
            description="Luar biasa mantap.",
            thumbnail="https://upload.wikimedia.org/wikipedia/en/7/73/Trollface.png?utm_source=en.wikipedia.org&utm_campaign=imageinfo&utm_content=thumbnail_unscaled",
            view="https://en.wikipedia.org/wiki/Trollface",
        )

    # main
    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    # experience
    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.description, "Membantu mahasiswa memahami pengembangan web.")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)
        self.assertFalse(self.experience.has_thumbnail)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    # project
    def test_project_model(self):
        self.assertEqual(str(self.project), "This Website")
        self.assertEqual(self.project.description, "Luar biasa mantap.")
        self.assertTrue(self.project.has_thumbnail)
        self.assertTrue(self.project.has_view)
        self.assertFalse(self.project.has_source)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_projects"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "projects.html")
        self.assertContains(response, self.project.title)
        self.assertContains(response, self.project.description)
        self.assertContains(response, "Thumbnail of This Website")
        self.assertContains(response, "https://en.wikipedia.org/wiki/Trollface")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_projects_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("main:show_projects"))

        self.assertContains(response, "Belum ada proyek yang ditambahkan.")

    def test_completed_projects(self):
        self.project.source = "https://en.wikipedia.org/w/index.php?title=Trollface&action=edit"
        self.project.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertTrue(self.project.has_source)
