from django.core.management import BaseCommand

from studies.models import Course
from users.models import Pays, User


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        user = list(User.objects.filter(id=1))[0]
        course = list(Course.objects.filter(id=2))[0]
        pay = Pays.objects.create(
            user=user,
            date_pay='2001-02-02',
            pay_course=course,
            summ_pay=30000,
            way_pay=0
        )

