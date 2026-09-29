from django.forms import ModelForm, TextInput, Textarea, URLInput, Select
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags

from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project

        fields = [
            "title",
            "description",
            "thumbnail",
            "view",
            "source",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "thumbnail": "URL Thumbnail Proyek",
            "view": "URL Proyek",
            "source": "URL Source Code Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Example: My Project",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Example: My new project.",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "Example: https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "view": URLInput(
                attrs={
                    "placeholder": "Example: https://my-project.com/",
                }
            ),
            "source": URLInput(
                attrs={
                    "placeholder": "Example: https://github.com/username/my-project",
                }
            ),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Project title cannot only be HTML tags.")
        return title

    def clean_description(self):
        description = strip_tags(self.cleaned_data["description"]).strip()
        if not description:
            raise ValidationError("Project description cannot only be HTML tags.")
        return description

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience

        fields = [
            "title",
            "description",
            "category",
            "thumbnail",
            # "started_at",
            # "ended_at",
        ]

        labels = {
            "title": "Judul Pengalaman",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Thumbnail Pengalaman",
            # "started_at": "Tanggal Memulai",
            # "ended_at": "Tanggal Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Example: Role Title",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Example: My role as X at Y.",
                    "rows": 3,
                }
            ),
            "category": Select(
                choices=Experience.EXPERIENCE_CHOICES,
                attrs={
                    "placeholder": "",
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "Example: https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            # "started_at"
            # "ended_at"
        }
