from django.db import models

# Create your models here.


class Banner(models.Model):
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return f"{self.pk}.{self.image}"

class GalleryCategory(models.Model):
    title = models.CharField(max_length=250, null=True, blank=False)

    def __str__(self):
        return f"{self.pk}.{self.title}"

class Media(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(blank=False, null=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"

    class Meta:
        verbose_name_plural = 'Media'

   
        



