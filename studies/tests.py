from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from studies.models import Lesson, Course
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test5@test.ru'
        )
        self.course = Course.objects.create(
            name='Testovoe21',
            overview='Test21',
            owner=self.user
        )
        self.lesson = Lesson.objects.create(
            name='Testovoe1',
            overview='Test',
            owner=self.user,
            course=self.course
        )

        self.client.force_authenticate(
            user=self.user
        )

    def test_create_lesson(self):
        """Тестирование создание урока"""
        data = model_to_dict(self.lesson, exclude=['picture', 'video'])
        response = self.client.post(
            '/studies/lesson/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_create_subscribe(self):
        """Тестирование создания подписки"""
        data = {
            "course_id": self.course.id
        }
        response = self.client.post(
            '/studies/subscribe/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_list_lesson(self):
        """Тестирование просмотра списка уроков"""
        response = self.client.get(
            '/studies/lesson/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_lesson(self):
        """Тестирование просмотра урока"""
        response = self.client.get(
            reverse('studies:lesson-get', args=[self.lesson.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """Тестирование изменения урока"""
        data = {
            "name": "Testovoe22",
            "overview": "Opyat Testovoe"
        }

        response = self.client.put(
            reverse('studies:lesson-update', args=[self.lesson.id]), data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        data = model_to_dict(self.lesson, exclude=['picture', 'video'])

        response1 = self.client.post(
            '/studies/lesson/create/',
            data=data
        )

        response = self.client.delete(
            reverse('studies:lesson-delete', args=[response1.json()['id']])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
