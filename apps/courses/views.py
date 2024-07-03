"""
views for courses and reviews endpoints
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework import mixins
from rest_framework.response import Response

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer

class CoursesAPIView(ListCreateAPIView):
    """
        API endpoint that list and create courses.
    """
    queryset = Course.objects.all()      
    serializer_class = CourseSerializer

class CourseAPIView(RetrieveUpdateDestroyAPIView):
    """
        API endpoint that retrieve, update and destroy a specific course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class ReviewsAPIView(ListCreateAPIView):
    """
        API endpoint that list and create review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id= self.kwargs.get('course_pk'))
        return self.queryset.all()

class ReviewAPIView(RetrieveUpdateDestroyAPIView):
    """
        API endpoint that retrieve, update and destroy a specific review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        if self.kwargs.get('course_pk') and self.kwargs.get('review_pk') :
            return get_object_or_404(self.queryset.all(), course_id=self.kwargs.get('course_pk'), pk=self.kwargs.get('review_pk'))
        return get_object_or_404(self.queryset.all(), pk=self.kwargs.get('pk'))
