from django.urls import path

from studies.views import (CourseViewSet, LessonCreateAPIView, LessonListAPIView,
                           LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView)

from studies.apps import StudiesConfig
from rest_framework.routers import DefaultRouter

app_name = StudiesConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
] + router.urls
