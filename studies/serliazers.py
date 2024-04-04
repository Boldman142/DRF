from rest_framework import serializers

from studies.models import Course, Lesson, Subscription
from studies.services import convert_price
from studies.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(many=True, read_only=True)
    usd_price = serializers.SerializerMethodField()
    subscribe = serializers.SerializerMethodField()

    def get_lesson_count(self, obj):
        return obj.lesson.count()

    def get_usd_price(self, instance):
        return convert_price(instance.price)

    def get_subscribe(self, obj):
        user = self.context['request'].user.pk
        return bool(Subscription.objects.filter(owner=user, course=obj.pk))


    class Meta:
        model = Course
        fields = ('id', 'name', 'lesson_count',
                  'lesson', 'overview', 'picture',
                  'owner', 'usd_price', 'subscribe')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
