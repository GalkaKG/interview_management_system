from django.test import TestCase
from interview_management_system.auth_app.models import CustomUser


class CustomUserModelTests(TestCase):
    def test_create_user(self):
        user = CustomUser(
            username='testuser',
            email='testuser@example.com',
            password='test_password123',
            is_superuser=False,
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.user_type, 'interviewer')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = CustomUser.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin_password123'
        )
        self.assertEqual(superuser.username, 'admin')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertEqual(superuser.user_type, 'interviewer')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)

    def test_user_str_method(self):
        user = CustomUser(username='testuser', email='testuser@example.com')
        self.assertEqual(str(user), 'testuser')

    def test_user_manager(self):
        user = CustomUser(
            username='testuser',
            email='testuser@example.com',
            password='test_password123'
        )
        user.save()

        self.assertTrue(CustomUser.objects.filter(username='testuser').exists())
