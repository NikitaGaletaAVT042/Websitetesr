# users/tests.py

from django.test import TestCase
from .models import CustomUser

class CustomUserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(username='testuser', email='test@example.com')

    def test_custom_user_creation(self):
        user = CustomUser.objects.get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
