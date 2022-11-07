from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from login import models

'''
@shared_task
def send_mail_task():
    print("Mail sending.......")
    subject = 'welcome to Celery world'
    message = 'Hi thank you for using celery'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['zhouzhouce@gmail.com', ]
    send_mail(subject, message, email_from, recipient_list)
    return "Mail has been sent........"
'''


@shared_task
def send_mail_task():
    subject = 'Daily training notification.'
    message = 'Hi, it is time for you to exercise.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = list(models.User.objects.values_list('email', flat=True))
    send_mail(subject, message, email_from, recipient_list)
