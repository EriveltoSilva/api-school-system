from rest_framework import serializers
from .models import Course, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email':{'write_only':True}
        }
        model = Review

        fields = (
            'id', 'course', 'name', 
            'email', 'comment', 'review', 
            'created_at', 'is_active'
        )

class CourseSerializer(serializers.ModelSerializer):
    # 1. Nested Relationship
    # reviews = ReviewSerializer(many=True, read_only=True)

    # 2. HyperLinked Related Field
    reviews = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='review')

    # 3. Primary key Related Field
    # reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Course
        fields = (
            'id', 'title', 'url', 'created_at', 'is_active', 'reviews'
        )
    