from django.test import TestCase
from interview_management_system.auth_app.models import CustomUser
from django.contrib.auth.models import Group


class CustomUserModelTests(TestCase):
    def test_create_user(self):
        user = CustomUser(
            username='testuser',
            email='testuser@example.com',
            password='test_password123',
            is_superuser=False,
            user_type='Interviewer',
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.user_type, 'Interviewer')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

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


class CustomUserGroupsTests(TestCase):
    def setUp(self):
        # Create the required user groups
        Group.objects.create(name='Administrator')
        Group.objects.create(name='HR')
        Group.objects.create(name='Interviewer')

    def test_administrator_user_is_staff(self):
        admin_user = CustomUser.objects.create(
            username='admin',
            email='admin@example.com',
            user_type='Administrator',
        )

        self.assertTrue(admin_user.is_staff)

    def test_non_administrator_user_is_not_staff(self):
        hr_user = CustomUser.objects.create(
            username='hr',
            email='hr@example.com',
            user_type='HR',
        )

        self.assertFalse(hr_user.is_staff)
