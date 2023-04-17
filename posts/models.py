from django.db import models





class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=250, null=True, blank=True)
    post_image = models.ImageField(upload_to="post/images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    details = models.TextField(blank=True, null=True)
    document = models.FileField(blank=True, null=True, upload_to="post/documents")

    
    def __str__(self):
        return self.title

