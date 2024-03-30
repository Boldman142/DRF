from django.db import models
from django.contrib.auth.models import AbstractUser

from studies.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='мыло')

    phone = models.CharField(
        max_length=35,
        verbose_name='номер телефона',
        **NULLABLE
    )
    country = models.CharField(
        max_length=50,
        verbose_name='страна',
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to='users/',
        verbose_name='аватар',
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ('email',)


class Pays(models.Model):
    class Conditions(models.IntegerChoices):
        TRANSFER = 0, 'Перевод на счет'
        CASH = 1, 'Наличные'

    user = models.ForeignKey(
        'User',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    date_pay = models.DateField(
        verbose_name='Дата платежа',
        **NULLABLE
    )
    pay_course = models.ForeignKey(
        'studies.Course',
        verbose_name='Оплаченный курс',
        on_delete=models.CASCADE,
        **NULLABLE
    )
    pay_lesson = models.ForeignKey(
        'studies.Lesson',
        verbose_name='Оплаченный урок',
        on_delete=models.CASCADE,
        **NULLABLE
    )
    summ_pay = models.PositiveIntegerField(
        verbose_name='Сумма платежа',
        **NULLABLE
    )
    way_pay = models.IntegerField(choices=Conditions.choices,
                                  default=0,
                                  verbose_name='способ оплаты'
                                  )

    # price_id = models.CharField(max_length=100, **NULLABLE)
    # product_id = models.CharField(max_length=100, **NULLABLE)
