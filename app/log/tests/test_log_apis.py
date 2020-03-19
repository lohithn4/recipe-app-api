import time

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from pinax.eventlog.models import Log, log

from tasks.tasks import create_log

#LOG_API = reverse('log-list')


class PublicLogApis(TestCase):
    """Test public log apis"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create(
            email='test@dummy.com', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_log_user_creation(self):
        #res = self.client.get(LOG_API)
        # userLogs = Log.objects.filter(user=self.user).first()
        # task = create_log.delay(None, "CREATE", extra={"cool": "now"})

        # print("task_id=", task.id)
        # print("task_status=", task.status)
        # print("task_status=", task.status)
        event = log(user=self.user, action="CREATE",
                    obj=self.user, extra={"cool": "now"})

        userLogs = Log.objects.all()[0]

        #self.assertEqual(res.status_code, status.HTTP_200_OK)
        #self.assertEqual(res.data['user'], self.user.email)
        self.assertEqual('CREATE', userLogs.action)
