from django.test import TestCase
from interview_management_system.auth_app.forms import CustomUserCreationForm
from interview_management_system.auth_app.models import CustomUser


class CustomUserCreationFormTests(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'user_type': 'interviewer',
            'password1': 'test_password123',
            'password2': 'test_password123',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_missing_field(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'user_type': 'interviewer',
            'password1': 'test_password123',
            # 'password2' is missing
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_invalid_form_password_mismatch(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'user_type': 'interviewer',
            'password1': 'test_password123',
            'password2': 'mismatched_password',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_save_creates_user(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'user_type': 'interviewer',
            'password1': 'test_password123',
            'password2': 'test_password123',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.user_type, 'interviewer')
