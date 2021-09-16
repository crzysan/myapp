"""Test django app."""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test.client import Client

# store the password to login later
PASSWORD = 'mypassword'
USERNAME = 'admin'
EMAIL = 'admin@myapp.com'

User = get_user_model()
ADMIN_USER = User.objects.create_superuser('$USERNAME', '$EMAIL', '$PASSWORD')


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser('$USERNAME', '$EMAIL', '$PASSWORD')

    def test_animals_can_speak(self):
        """Users that exists are correctly identified"""
        client = Client()
        admin_user = User.object.get(username="admin")
        self.assertEqual(client.login(username=admin_user.username, password=admin_user.password),
                         'Admin user is logged in and says "Hello!"')
