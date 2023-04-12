"""leadspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.serializers import CustomJWTSerializer
from django.urls import path
from django.urls import path, include, re_path as url
from . import settings
from django.conf.urls.static import static
from django.views.static import serve
#from accounts.views import current_user
from .routers import router
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from rest_framework import permissions

#password reset
from password_recover import views

#event register
from events.views import(
    EventRegisterViewSet
)

from accounts.views import(
    AccountViewSet,
    Profile
    
)

from accounts.views import(
    VerifyOTPview,
    LoginView
)





class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=True):
        schema = super().get_schema(request, public)
        schema.schemes = ["http", "https"]
        return schema 


schema_view = get_schema_view(
   openapi.Info(
      title="RVK webportal api",
      default_version='v1',
      description="Documentation for Rvk webportal Api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="bernardnamangala@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes = (permissions.AllowAny,),
   generator_class=BothHttpAndHttpsSchemaGenerator
)


urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),

    #account
    #path('api/token/', TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer),name='token_obtain_pair'),

    #path('api/token/refresh/', TokenRefreshView.as_view(serializer_class=CustomJWTSerializer),name='token_refresh'),
    path('api/accounts/', AccountViewSet.as_view()),
    path('api/verify-account/', VerifyOTPview.as_view()),
    path('api/login/', LoginView.as_view()),
    path('api/profile/', Profile.as_view()),
    
    
    #path("api/current_user/", current_user),
    path('api/', include(router.urls)),
    
    path('ckeditor', include('ckeditor_uploader.urls')),


    path('', include('ckeditor_uploader.urls')),


    #password_recover
    path('', include("password_recover.urls")),
    

    #payments
    path('api/', include("payment_methodology.urls")),
    path('api/', include("events.urls")),

    #event register




    
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

