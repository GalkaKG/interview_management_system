from __future__ import absolute_import, unicode_literals

from datetime import datetime

from celery import shared_task

from interview_management_system.interview_management.models import Interview

from django.utils import timezone

from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)


@shared_task(bind=True)
def add(x, y):
    return x + y


@shared_task
def update_interview_statuses():
    logger.info("Celery task update_interview_statuses is running")
    current_datetime = timezone.now()
    current_date = current_datetime.date()  # Get the date (YYYY-MM-DD)
    current_time = current_datetime.time()  # Get the time (HH:MM:SS)

    # Find interviews scheduled for the future
    scheduled_interviews = Interview.objects.filter(status='Scheduled', date__gt=current_date)

    for interview in scheduled_interviews:
        # Combine the date and time fields to create a datetime object for the interview
        interview_datetime = datetime.combine(interview.date, interview.time)

        # Calculate the time remaining until the interview's scheduled time
        time_until_interview = interview_datetime - current_datetime

        if time_until_interview.total_seconds() <= 0:
            # The scheduled time has come, change status to 'InProgress'
            interview.status = 'InProgress'
            interview.save()
        elif time_until_interview.total_seconds() <= 600:  # 10 minutes
            # 10 minutes have passed, change status to 'Completed'
            interview.status = 'Completed'
            interview.save()

    logger.info("Celery task update_interview_statuses finished")

# @shared_task
# def update_interview_statuses():
#     now = datetime.now()
#     # Update the status of interviews that are scheduled to start
#     interviews_to_update = Interview.objects.filter(date__lte=now.date(), time__lte=now.time(), status='Scheduled')
#     interviews_to_update.update(status='InProgress')
