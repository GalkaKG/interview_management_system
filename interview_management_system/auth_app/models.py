from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import Group


class CustomUserManager(BaseUserManager):
    def create_interviewer(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

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
        ('Administrator', 'Administrator'),
        ('HR', 'HR'),
        ('Interviewer', 'Interviewer')
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, )

    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.user_type == 'Administrator':
            self.is_staff = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    department = models.CharField(max_length=30, blank=True, null=True)

    def save(self, *args, **kwargs):

        if self.user.user_type:
            group = Group.objects.get(name=self.user.user_type)
            self.user.groups.add(group)

        super().save(*args, **kwargs)



