from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class PremRawatAboutBanner(models.Model):
    title = models.CharField(max_length=250, null=True, blank=False)
    sub_title = models.CharField(max_length=250, null=True, blank=False)
    image = models.ImageField(blank=False, null=True, upload_to="media/about/banner")

    def __str__(self):
        return f"{self.pk}.{self.title}"
    
    class Meta:
        verbose_name_plural = 'Banners'
    
class PremRawattDescription(models.Model):
    first_section_description = RichTextUploadingField(blank=True, null=True, verbose_name="First Section Description")
    first_section_img = models.ImageField(null=True, blank=False, verbose_name="First Section Image")

    second_section_description = RichTextUploadingField(blank=True, null=True, verbose_name="Second Section Description")
    second_section_img = models.ImageField(null=True, blank=False, verbose_name="Second Section Image")

    thired_section_description = RichTextUploadingField(blank=True, null=True, verbose_name="Third Section Description")
    third_section_img = models.ImageField(null=True, blank=False, verbose_name="Third Section Image")

    fourth_section_description = RichTextUploadingField(blank=True, null=True, verbose_name="Third Section Description")
    fourth_section_img = models.ImageField(null=True, blank=False, verbose_name="Fourth Section Image")

    def __str__(self):
        return f"{self.pk}.{self.first_section_description}"
    
    class Meta:
        verbose_name_plural = 'Description'

