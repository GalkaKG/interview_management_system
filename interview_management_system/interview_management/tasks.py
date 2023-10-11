# tasks.py

from celery import Celery
from datetime import datetime, timedelta

from interview_management_system.interview_management.models import Interview

app = Celery('interview_management')
app.config_from_object('django.conf:settings')


@app.task
def update_interview_statuses():
    now = datetime.now()
    scheduled_interviews = Interview.objects.filter(
        status='Scheduled',
        date__lte=now.date(),
        time__lte=(now - timedelta(minutes=30)).time()
    )

    for interview in scheduled_interviews:
        interview.status = 'Completed'
        interview.save()

        # Send a message to the interviewer to prompt for feedback using RabbitMQ.
        # You'll need to implement your own logic to send messages.






from celery import shared_task

from interview_management_system.interview_management.models import Interview
from datetime import datetime, timedelta


@shared_task
def send_interview_notification(interview_id):
    try:
        # Retrieve the interview object
        interview = Interview.objects.get(pk=interview_id)

        # Calculate the time until the interview
        current_time = datetime.now()
        interview_time = datetime.combine(interview.date, interview.time)
        time_until_interview = interview_time - current_time

        # Set a threshold (e.g., 30 minutes) for sending notifications
        notification_threshold = timedelta(minutes=30)

        if time_until_interview <= notification_threshold:
            # Notify the user (replace this with your notification logic)
            notify_user(interview.candidate.email,
                        f'Your interview is starting soon for {interview.date} at {interview.time}.')

    except Interview.DoesNotExist:
        # Handle the case where the interview doesn't exist
        pass


def notify_user(email, message):
    # Replace this with your notification logic (e.g., send an email, push notification, or in-app notification)
    # Here, we're using a simple print statement as a placeholder
    print(f'Sending notification to {email}: {message}')
