from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from studies.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


# class LessonAllSerializer(serializers.ModelSerializer):
#     count = serializers.SerializerMethodField()
#     lesson = SlugRelatedField(slug_field='lesson', queryset=Lesson.objects.all())
#     def get_count(self, obj):
#         return obj.lesson.count()
#
#     class Meta:
#         model = Lesson
#         fields = ('count', 'lesson')


# class CourseListSerializer(serializers.ModelSerializer):
#     lesson_count = serializers.SerializerMethodField()
#     lesson = SlugRelatedField(slug_field='lesson', queryset=Lesson.objects.all())
#
#     def get_lesson_count(self, obj):
#         return obj.lesson_set.count()
#
#     class Meta:
#         model = Course
#         fields = ('name', 'lesson_count', 'lesson', 'overview', 'picture')


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    class Meta:
        model = Course
        fields = ('name', 'lesson_count', 'lesson', 'overview', 'picture', 'owner')
