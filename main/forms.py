from django.forms import ModelForm, TextInput, Textarea, URLInput

from main.models import Project

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
                    "placeholder": "My Project",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "New Project",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://drive.google.com/thumbnail?id=...&sz=w1000",
                }
            ),
            "view": URLInput(
                attrs={
                    "placeholder": "https://my-project.com/",
                }
            ),
            "source": URLInput(
                attrs={
                    "placeholder": "https://github.com/username/my-project",
                }
            ),
        }
