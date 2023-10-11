from django import forms

from interview_management_system.interview_management.models import Candidate, Interview


class AddCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['candidate', 'interviewer', 'date_time', 'status']

    widgets = {
        'date_time': forms.DateInput(attrs={'type': 'date'}),
    }
