from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, generics

from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from studies.models import Course, Lesson, Subscription
from studies.paginators import ListPaginator
from studies.serliazers import CourseSerializer, LessonSerializer
from studies.permissions import Moderator, IsOwner
from studies.services import Stripe_API

from studies.tasks import send_mail_change


class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для курсов """
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

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        send_mail_change.delay(request.get('id'))


class LessonCreateAPIView(generics.CreateAPIView):
    """APIView для создания урока"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~Moderator]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """APIView для просмотра списка уроков"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~Moderator]

    filter_backends = [OrderingFilter]
    ordering_fields = ('id',)
    pagination_class = ListPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """APIView для просмотра одного урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, Moderator | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    """APIView для изменения урока"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, Moderator | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """APIView для удаления урока"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwner | ~Moderator]


class SubscriptionAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="APIView для создания/удаления подписки на курс"
    )
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


class StripeAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        course_id = kwargs.get('pk')
        course = get_object_or_404(Course, id=course_id)
        stripe_API = Stripe_API()
        if course.price_id is None or course.product_id is None:
            price = stripe_API.create_product(course.name, course.price)
            course.price_id = price['id']
            course.product_id = price['product']
            course.save()
        session = stripe_API.create_session(course.price_id)
        return Response({'url': session.url})
