from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Banner(models.Model):
    img = models.ImageField(upload_to="home/banner", null=True, blank=False)

    def __str__(self):
        return f"{self.pk}.{self.img}"
    
class LatestVideo(models.Model):
    thumbnail = models.ImageField(blank=False, null=True)
    video_link = models.CharField(max_length=350, null=True, blank=False, verbose_name='Video Link')
    play_list_link = models.CharField(max_length=350, null=True, blank=False, verbose_name='Video Playlist Link')

    def __str__(self):
        return f"{self.pk}.{self.video_link}"
    
    class Meta:
        verbose_name_plural = 'Latest Videos'


INITIATIVE_CATEGORY =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)

# class Initiative(models.Model):
#     title = forms.ChoiceField(choices = GEEKS_CHOICES)


# class Initiative(models.Model):
#     title = models.CharField(max_length=350, null=True, blank=False)
#     sub_title = models.CharField(max_length=350, null=True, blank=True)
#     img = models.ImageField(blank=False, null=True)

#     #details = RichTextUploadingField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.pk}.{self.title}"
    
class NewsShelter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.pk}.{self.email}"
    
    class Meta:
        verbose_name_plural = 'News Shelter'

    
