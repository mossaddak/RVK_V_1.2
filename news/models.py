from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class NewsCategory(models.Model):
    title = models.CharField(max_length=250, null=True, blank=False)

    def __str__(self):
        return f"{self.pk}.{self.title}"
    
    class Meta:
        verbose_name_plural = 'News Categories'

class News(models.Model):
    news_category = models.ForeignKey(NewsCategory, on_delete = models.CASCADE, null=True)
    title = models.CharField(max_length=350, null=True, blank=False)
    image = models.ImageField(blank=False, null=True)
    details = models.TextField(blank=True, null=True)
    news_document = models.FileField(null=True, blank=False, verbose_name="news document")
    author = models.CharField(max_length=250, null=True)

    created_at = models.DateTimeField( null=True)

    def __str__(self):
        return f"{self.pk}.{self.title}"
    
    class Meta:
        verbose_name_plural = 'Newses'
