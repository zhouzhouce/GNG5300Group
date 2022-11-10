from django.test import TestCase
import rest_framework
from login import models
from django.core import mail


# Create your tests here.
class TestScheduledNotification(TestCase):
    def test_list_emails(self):
        user1 = models.User(email='zhouzhouce@gmail.com', password='123456')
        user1.save()
        recipient_list = list(models.User.objects.values_list('email', flat=True))
        assert len(recipient_list) == 1
        assert recipient_list == ['zhouzhouce@gmail.com']

    def test_send_email(self):
        mail.send_mail('Subject here', 'Here is the message.',
                       'zhouzhouce@gmail.com', ['zhouzhouce@gmail.com'],
                       fail_silently=False)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')
