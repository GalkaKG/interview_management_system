from django import forms
from django.contrib.auth.forms import UserCreationForm

from interview_management_system.auth_app.models import CustomUser, Interviewer, DEPARTMENT_CHOICES, HR


class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label='Type password:')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password'}), label='Retype password:')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'user_type']


class EditInterviewerProfileForm(forms.ModelForm):
    class Meta:
        model = Interviewer
        exclude = ('user',)


class EditHRProfileForm(forms.ModelForm):
    class Meta:
        model = HR
        exclude = ('user',)

