from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_interviewer(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        # # Create an associated user type instance
        # if user_type == 'interviewer':
        #     Interviewer.objects.create(user=user, **extra_fields)
        # elif user_type == 'hr':
        #     HR.objects.create(user=user, **extra_fields)

        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_interviewer(username, email, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    USER_TYPES = (
        ('interviewer', 'Interviewer'),
        ('hr', 'HR'),
        ('admin', 'Administrator'),
    )
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='interviewer')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


DEPARTMENT_CHOICES = (
    ('HR', 'Human Resources'),
    ('IT', 'Information Technology'),
    ('SALES', 'Sales'),
)


class Interviewer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.user.username


class HR(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.user.username

# from django.contrib.auth.models import Permission
#
# # Create custom permissions
# can_view_candidate = Permission.objects.create(
#     codename='can_view_candidate',
#     name='Can view candidate details'
# )
# can_schedule_interview = Permission.objects.create(
#     codename='can_schedule_interview',
#     name='Can schedule interviews'
# )
#
# # Assign permissions to roles
# interviewer = Group.objects.get(name='interviewer')
# hr = Group.objects.get(name='hr')
# admin = Group.objects.get(name='admin')
# interviewer.permissions.add(can_view_candidate)
# hr.permissions.add(can_view_candidate, can_schedule_interview)
# admin.permissions.add(can_view_candidate, can_schedule_interview)


# from django.contrib.auth.models import Group
#
# def assign_user_role(user, role):
#     group = Group.objects.get(name=role)
#     user.groups.add(group)
#
# # Example: Assign a user the role of 'interviewer'
# assign_user_role(user, 'interviewer')




# from django.contrib.auth.decorators import permission_required
#
# @permission_required('auth.can_schedule_interview')
# def schedule_interview(request):
#     # Your view logic here

