from django import forms
from django.contrib.auth.forms import UserCreationForm

from interview_management_system.auth_app.models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label='Type password:')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label='Retype password:')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)


# class EditHRProfileForm(forms.ModelForm):
#     class Meta:
#         model = HR
#         exclude = ('user',)
#
#
# class EditAdministratorForm(forms.ModelForm):
#     class Meta:
#         model = Administrator
#         exclude = ('user', 'is_superuser', 'is_staff')
