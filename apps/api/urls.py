"""
URL for api endpoints .
The `urlpatterns` list routes URLs to views. 
"""

from django.urls import path
from apps.courses import views as views_courses

urlpatterns = [
    path('courses/', views_courses.CoursesAPIView.as_view(), name="courses"),
    path('courses/<int:pk>/', views_courses.CourseAPIView.as_view(), name="course"),

    path('reviews/', views_courses.ReviewsAPIView.as_view(), name="reviews"),
    path('reviews/<int:pk>/', views_courses.ReviewAPIView.as_view(), name="review"),
    
    path('courses/<int:pk>/reviews/', views_courses.ReviewsAPIView.as_view(), name="course-reviews"),
    path('courses/<int:course_pk>/reviews/<int:review_pk>', views_courses.ReviewsAPIView.as_view(), name="course-reviews"),
]
