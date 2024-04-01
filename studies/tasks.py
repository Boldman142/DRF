from celery import shared_task
from django.core.mail import send_mail

from core import settings
from studies.models import Subscription
from users.models import User


@shared_task
def send_mail_change(pk):
    all_subs = Subscription.objects.filter(course_id=pk)
    recipients = []
    for sub in all_subs:
        user = User.objects.get(id=sub.owner_id)
        email_user = user.email
        recipients.append(email_user)
    if len(recipients) > 0:
        send_mail(
            subject='Изменения в курсе',
            message='Курс на который вы подписаны изменился',
            recipient_list=recipients,
            from_email=settings.EMAIL_ADMIN
        )
