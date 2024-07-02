"""
URL for api endpoints .
The `urlpatterns` list routes URLs to views. 
"""

from django.urls import path, include
from apps.courses import views as views_courses

urlpatterns = [
    path('courses/', views_courses.CourseAPIView.as_view(), name='courses'),
    path('reviews/', views_courses.ReviewAPIView.as_view(), name='reviews'),
]