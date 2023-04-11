from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    phone = models.CharField(max_length=25)

    def __str__(self):
        return self.name
