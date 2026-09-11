from django.shortcuts import render

from main.models import Experience
from main.models import Project


def show_main(request):
    context = {
        "name": "Axel Sebastian Saragih",
        "npm": "2506590063",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Second-year CS student at Universitas Indonesia. "
            "Interested in the world of Cybersecurity and Game Development."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Axel Sebastian Saragih",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)


def show_projects(request):
    context = {
        "name": "Axel Sebastian Saragih",
        "project_list": Project.objects.all(),
    }
    return render(request, "projects.html", context)
