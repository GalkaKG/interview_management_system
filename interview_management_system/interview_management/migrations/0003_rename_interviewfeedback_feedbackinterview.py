# Generated by Django 4.2.6 on 2023-10-12 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview_management', '0002_job_interviewfeedback_overall_result'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InterviewFeedback',
            new_name='FeedbackInterview',
        ),
    ]
