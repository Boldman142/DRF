from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LessonTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = reverse('/studies/lesson/create/')
        self.data = {
            "name": "Testovoe",
            "overview": "Opyat Testovoe"
        }

    # def test_create_lesson(self):
    #     """Тестирование создание урока"""
    #     data = {
    #         "name": "Testovoe",
    #         "overview": "Opyat Testovoe"
    #     }
    #     self.client.post(
    #         '/studies/lesson/create/',
    #         data=data
    #     )
    #
    #     self.assertEqual(
    #         response.status_code,
    #         status.HTTP_201_CREATED
    #     )

    def test_get_lesson(self):
        """Тестирование просмотра урока"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_list_lesson(self):
    #     """Тестирование просмотра списка уроков"""
    #     pass
    #
    # def test_update_lesson(self):
    #     """Тестирование изменения урока"""
    #     pass
    #
    # def test_delete_lesson(self):
    #     """Тестирование удаления урока"""
    #     pass
