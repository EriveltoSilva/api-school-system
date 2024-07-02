from django.contrib import admin
from .models import Course, Review
# Register your models here.

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'url', 'is_active','created_at']
    list_display_links = ['id', 'title', 'url', 'created_at']
    list_per_page = 25


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'name', 'review','created_at']
    list_display_links = ['id', 'course', 'name','review', 'created_at']
    list_per_page = 25
    