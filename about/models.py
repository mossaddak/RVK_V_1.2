from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class RvkAboutBanner(models.Model):
    title = models.CharField(max_length=250, null=True, blank=False)
    sub_title = models.CharField(max_length=250, null=True, blank=False)
    image = models.ImageField(blank=False, null=True, upload_to="media/about/banner")

    def __str__(self):
        return f"{self.pk}.{self.title}"
    
    class Meta:
        verbose_name_plural = 'Banners'
    
class RvkAboutDescription(models.Model):
    first_section_description = models.TextField(blank=True, null=True, verbose_name="First Section Description")
    first_section_img = models.ImageField(null=True, blank=False, verbose_name="First Section Image")

    second_section_description = models.TextField(blank=True, null=True, verbose_name="Second Section Description")
    second_section_img = models.ImageField(null=True, blank=False, verbose_name="Second Section Image")

    thired_section_description = models.TextField(blank=True, null=True, verbose_name="Third Section Description")

    def __str__(self):
        return f"{self.pk}.{self.first_section_description}"
    
    class Meta:
        verbose_name_plural = 'Description'

class QuickLinks(models.Model):
    image = models.ImageField(null=True, blank=False)
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return f"{self.pk}.{self.description}"
    
    class Meta:
        verbose_name_plural = 'Quick Links'