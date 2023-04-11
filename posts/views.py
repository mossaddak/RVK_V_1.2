from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from RVK_WEBPORTAL.permissions import ReadOnly
from RVK_WEBPORTAL.pagination import CustomPagination

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_fields = ("category__name", "author__name", "")
    permission_classes = [ReadOnly,]
    pagination_class = CustomPagination
    

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)