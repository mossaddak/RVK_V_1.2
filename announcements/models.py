from django.db import models


class Announcement(models.Model):
    content = models.TextField()

    def __str__(self):
        return f"{self.pk}.{self.content}"