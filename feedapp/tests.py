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

    def test_admin_login(self):
        """Users that exists are correctly identified"""
        client = Client()
        response = client.post('/admin/login/', {'username': 'USERNAME', 'password': '$PASSWORD'})
        print(response.status_code)
        response = client.get('/admin/feedapp/user/')
        print(response.content)
   
    def test_create_post(self):
        client = Client()
        test_user =  User.objects.create_superuser("test", "test@myapp", "test")
        print(test_user)
        #response = client.post('/', {'user': 'test_user', 'text': "This is a test"})
        #print(response.status_code)

