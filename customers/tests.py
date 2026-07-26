from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from measurements.models import FurnitureDimension
from .models import Customer


class CustomerViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='pass')
        self.customer = Customer.objects.create(full_name='Rajesh Kumar', phone='+91 98765 43210', city='Jaipur')
        FurnitureDimension.objects.create(customer=self.customer, furniture_type='sofa', values={'Width': '40'})

    def test_phone_lookup_normalizes_phone_and_returns_measurements(self):
        response = self.client.get(reverse('api_get_customer_by_phone', args=['+91-98765-43210']))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['customer']['phone'], '+919876543210')
        self.assertEqual(data['measurements']['sofa']['values']['Width'], '40')
