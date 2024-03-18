from django.db import models
from django.conf import settings

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название курса')
    overview = models.TextField(verbose_name='Описание курса')
    picture = models.ImageField(upload_to='catalog/', **NULLABLE)
    owner = models.ForeignKey('users.User', verbose_name='владелец',
                              on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey('Course', verbose_name='Курс',
                               on_delete=models.CASCADE, related_name='lesson', **NULLABLE)
    name = models.CharField(max_length=50, verbose_name='Название урока')
    overview = models.TextField(verbose_name='Описание Урока')
    picture = models.ImageField(upload_to='catalog/', **NULLABLE)
    video = models.TextField(verbose_name='Ссылка на видео?', **NULLABLE)
    owner = models.ForeignKey('users.User', verbose_name='владелец',
                              on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
