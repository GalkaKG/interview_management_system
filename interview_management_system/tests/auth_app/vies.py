from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from interview_management_system.auth_app.forms import CustomUserCreationForm
from interview_management_system.auth_app.models import CustomUser


class RegisterViewIntegrationTests(TestCase):
    def test_register_view(self):
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'user_type': 'interviewer',
            'password1': 'test_password123',
            'password2': 'test_password123',
        }

        url = reverse('register')

        response = self.client.post(url, user_data)

        self.assertEqual(response.status_code, 302)

        user = CustomUser.objects.filter(email=user_data['email']).first()
        self.assertIsNotNone(user)

        self.assertTrue(response.wsgi_request.user.is_authenticated)


