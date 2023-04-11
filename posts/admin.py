from django.contrib import admin
from .models import Post, PostAction, PostCategory , PostStatus


admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(PostAction)
admin.site.register(PostStatus)