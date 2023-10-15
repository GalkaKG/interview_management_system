from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group


class RegisterViewIntegrationTests(TestCase):
    def setUp(self):
        Group.objects.create(name='Administrator')
        Group.objects.create(name='HR')
        Group.objects.create(name='Interviewer')

    def test_register_view_success(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'test_password123',
            'password2': 'test_password123',
            'user_type': 'HR'
        }

        url = reverse('register')

        response = self.client.post(url, user_data, follow=True)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.wsgi_request.user.is_authenticated)

        self.assertRedirects(response, reverse('home'))

    def test_register_view_failure(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'test_password123',
            'password2': 'incorrect_password',
        }

        url = reverse('register')

        response = self.client.post(url, user_data)

        self.assertEqual(response.status_code, 200)

        self.assertFalse(response.wsgi_request.user.is_authenticated)