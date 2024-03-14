from django.core.management import BaseCommand
from users.models import Pays


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        pay = Pays.objects.create(
            user=1,
            date_pay='01.01.2001',
            pay_course=1,
            summ_pay=10000,
            way_pay=1
        )

