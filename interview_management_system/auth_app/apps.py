from django.apps import AppConfig


class AuthAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'interview_management_system.auth_app'

    def ready(self):
        import interview_management_system.auth_app.signals
