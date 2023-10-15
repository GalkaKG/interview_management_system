from django.contrib import admin

from interview_management_system.auth_app.models import CustomUser, Profile


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ['username', 'is_superuser']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

