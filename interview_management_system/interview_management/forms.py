from datetime import datetime

from django import forms

from interview_management_system.interview_management.models import Candidate, Interview, FeedbackInterview, Job


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['published_at']

        widgets = {
            'description': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Add description...'}
            ),
            'requirements': forms.Textarea(
                attrs={'rows': 5, 'placeholder': 'Add requirements...'}
            ),
        }


class AddCandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['job', 'candidate', 'interviewer', 'date', 'time']

    date = forms.DateField(
        initial=datetime.now().strftime("%Y-%m-%d"),
        widget=forms.widgets.DateInput(
            attrs={'type': 'date'})
    )

    time = forms.CharField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )


class FeedbackInterviewForm(forms.ModelForm):
    class Meta:
        model = FeedbackInterview
        fields = '__all__'

        widgets = {
            'feedback_text': forms.Textarea(attrs={'rows': 4}),
        }


class EditInterviewStatusForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['status']
