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
        self.lesson = Lesson.objects.create(
            name='Testovoe1',
            overview='Test',
            owner=self.user
        )
        self.course = Course.objects.create(
            name='Testovoe21',
            overview='Test21',
            owner=self.user
        )
        self.client.force_authenticate(
            user=self.user
        )

    def test_create_lesson(self):
        """Тестирование создание урока"""
        data = {
            "name": "Testovoe",
            "overview": "Opyat Testovoe"
        }

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
        # response = (
        #     self.client.get(
        #         '/studies/lesson/1/'
        #     ))

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
        # response = self.client.put(
        #     '/studies/lesson/update/1/',
        #     data=data
        # )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        response = self.client.delete(
            reverse('studies:lesson-delete', args=[self.lesson.id])
        )
        # response = self.client.delete(
        #     '/studies/lesson/delete/1/',
        # )
        print(self.client)
        print(self.user)
        print(self.lesson.owner)
        print(response.json())

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
