"""
URL configuration for setup project.
The `urlpatterns` list routes URLs to views. 
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
