from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class CoreViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='pass')

    def test_dashboard_loads(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
