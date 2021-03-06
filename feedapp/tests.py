"""
Test django app.
source: https://docs.djangoproject.com/en/3.2/topics/testing/overview/
source: https://docs.djangoproject.com/en/3.2/topics/testing/tools/
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client

# store the password to login later
PASSWORD = 'mypass'
USERNAME = 'testuser'
EMAIL = 'testuser@myapp.com'

User = get_user_model()

# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create_superuser('$USERNAME', '$EMAIL', '$PASSWORD')

    @classmethod
    def test_admin_login(cls):
        """Users that exists are correctly identified"""
        client = Client()
        response = client.post('/admin/login/', {'username': 'USERNAME', 'password': 'PASSWORD'})
        print(response)
        return response.status_code
