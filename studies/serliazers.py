from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from studies.models import Course, Lesson, Subscription
from studies.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = ('name', 'lesson_count', 'lesson', 'overview', 'picture', 'owner')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
