from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.title}"