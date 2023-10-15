from django.db import models
from django.utils import timezone

from interview_management_system.auth_app.models import Interviewer, CustomUser
from . import custom_validators


class Job(models.Model):
    JOBS_TITLES = (
        ('developer', 'Software Developer'),
        ('designer', 'Graphic Designer'),
        ('manager', 'Project Manager'),
        ('analyst', 'Business Analyst'),
        ('engineer', 'Mechanical Engineer'),
    )
    title = models.CharField(max_length=100, choices=JOBS_TITLES)
    location = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    published_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.title


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    resume_url = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Candidates"


class Interview(models.Model):
    STATUS_CHOICES = (
        ('Scheduled', 'Scheduled'),
        ('InProgress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    date = models.DateField(validators=(custom_validators.future_date_validator,))
    time = models.TimeField(validators=(custom_validators.future_time_validator,))
    status = models.CharField(max_length=20, default='Scheduled', choices=STATUS_CHOICES)

    def __str__(self):
        return f"Interview for {self.candidate} with {self.interviewer} on {self.date} in {self.time}"


class FeedbackInterview(models.Model):
    RESULT = (
        ('Positive', 'Positive'),
        ('Negative', 'Negative'),
        ('Canceled', 'Canceled'),
        ('None', 'None'),
    )
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)




# class Notification(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     content = models.CharField(max_length=255)
#     is_read = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.content
