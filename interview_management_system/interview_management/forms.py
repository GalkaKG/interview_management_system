from datetime import datetime

from django import forms

from interview_management_system.interview_management.models import Candidate, Interview


class AddCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['candidate', 'interviewer', 'date', 'time', 'status']

    date = forms.DateField(
        initial=datetime.now().strftime("%Y-%m-%d"),
        widget=forms.widgets.DateInput(
            attrs={'type': 'date'})
    )

    time = forms.CharField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

