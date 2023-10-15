from django.test import TestCase
from interview_management_system.auth_app.forms import CustomUserCreationForm


class CustomUserCreationFormTests(TestCase):
    def test_valid_form(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
            'user_type': 'Administrator',
        }
        form = CustomUserCreationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword123',
            'password2': 'wrongpassword',
            'user_type': 'InvalidUserType',
        }
        form = CustomUserCreationForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)
