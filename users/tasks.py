import datetime

from celery import shared_task

from users.models import User


@shared_task
def deactivate_not_active():
    users = User.objects.all()
    date_now = datetime.date
    for user in users:
        if user.last_login:
            not_login = (date_now - user.last_login.date).days
        else:
            not_login = (date_now - user.date_joined.date).days
        if not_login > 30:
            user.is_active = False
