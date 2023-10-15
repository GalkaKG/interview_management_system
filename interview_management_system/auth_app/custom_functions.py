from django.shortcuts import redirect

from interview_management_system.auth_app.models import CustomUser


def get_custom_user(pk):
    try:
        user = CustomUser.objects.get(id=pk)
        return user
    except CustomUser.DoesNotExist:
        return redirect('error_404')

