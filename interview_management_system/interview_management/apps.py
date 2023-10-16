from django.apps import AppConfig


class InterviewManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'interview_management_system.interview_management'

    def ready(self):
        import interview_management_system.interview_management.signals
        