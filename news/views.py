from rest_framework.permissions import (
    BasePermission, SAFE_METHODS
)
from rest_framework import (
    parsers,
)

from rest_framework.viewsets import(
    ModelViewSet
)
from .models import(
    NewsCategory,
    News,
    NewsBanner
)
from .serializer import(
    NewsSerializer,
    NewsCategorySerializer,
    NewsBannerSerializer
)

from RVK_WEBPORTAL.permissions import (
    IsContentEditor
)


# Create your views here.
# class ReadOnlyPermission(BasePermission):
#     def has_permission(self, request, view):
#         return request.method in SAFE_METHODS
    

class NewsCategoryModelView(ModelViewSet):
    serializer_class = NewsCategorySerializer
    queryset = NewsCategory.objects.all()
    permission_classes = [IsContentEditor]
    

    
class NewsModelView(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class RecentNewsModelView(ModelViewSet):
    serializer_class = NewsSerializer
    queryset = News.objects.all()[:4] 
    permission_classes = [IsContentEditor]
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]

class NewsBannerModelView(ModelViewSet):
    serializer_class = NewsBannerSerializer
    queryset = NewsBanner.objects.all()
    permission_classes = [IsContentEditor]




