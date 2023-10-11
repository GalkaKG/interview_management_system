from django.db import models

from interview_management_system.auth_app.models import Interviewer


class Candidate(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
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
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    interviewer = models.ForeignKey(Interviewer, on_delete=models.CASCADE)
    date_time = models.DateField()
    time = models.TimeField(default='00:00:00')
    status = models.CharField(max_length=20, default='Scheduled', choices=STATUS_CHOICES)  # You can define interview status choices

    def __str__(self):
        return f"Interview for {self.candidate} with {self.interviewer} on {self.date_time}"


class InterviewFeedback(models.Model):
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)


