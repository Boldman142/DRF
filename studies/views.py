from rest_framework import viewsets, generics

from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from studies.models import Course, Lesson, Subscription
from studies.paginators import ListPaginator
from studies.serliazers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from studies.permissions import Moderator, IsOwner


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = ListPaginator

    def get_permissions(self):
        if self.action == 'CREATE':
            self.permission_classes = [IsAuthenticated, ~Moderator]
        elif self.action in ['GET', 'PUT', 'PATCH']:
            self.permission_classes = [Moderator | IsOwner]
        elif self.action == 'DELETE':
            self.permission_classes = [~Moderator, IsOwner]

        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~Moderator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~Moderator]

    filter_backends = [OrderingFilter]
    ordering_fields = ('id',)
    pagination_class = ListPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, Moderator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, Moderator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~Moderator, IsOwner]


class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)
        subs_item = Subscription.objects.filter(owner=user, course=course_item)
        if subs_item:
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(owner=user, course=course_item)
            message = 'подписка добавлена'

        return Response({"message": message})
