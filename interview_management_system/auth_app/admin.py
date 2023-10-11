from django.contrib import admin

from interview_management_system.auth_app.models import CustomUser, Interviewer, HR


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_filter = ['username', 'is_superuser']


@admin.register(Interviewer)
class InterviewerAdmin(admin.ModelAdmin):
    pass


@admin.register(HR)
class HRAdmin(admin.ModelAdmin):
    pass
