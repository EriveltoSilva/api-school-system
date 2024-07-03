"""
views for courses and reviews endpoints
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer

class CoursesAPIView(ListCreateAPIView):
    """
        API endpoint that list and create courses.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (AllowAny,)

class CourseAPIView(RetrieveUpdateDestroyAPIView):
    """
        API endpoint that retrieve, update and destroy a specific course.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ReviewsAPIView(ListCreateAPIView):
    """
        API endpoint that list and create review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        if self.kwargs.get('course_pk') and self.kwargs.get('review_pk') :
            return get_object_or_404(
                self.queryset.all(),
                course_id=self.kwargs.get('course_pk'),
                pk=self.kwargs.get('review_pk')
            )
        return get_object_or_404(self.queryset.all(), pk=self.kwargs.get('pk'))
