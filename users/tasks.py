from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def deactivate_not_active():
    users = User.objects.filter(is_active=True,
                                last_login__lt=timezone.now() - timezone.timedelta(days=30))
    users.update(is_active=False)
    # users = User.objects.filter(is_active=True)
    # date_now = datetime.date
    # for user in users:
    #     if user.last_login:
    #         not_login = (date_now - user.last_login.date).days
    #     else:
    #         not_login = (date_now - user.date_joined.date).days
    #     if not_login > 30:
    #         user.is_active = False
    #         user.save()
