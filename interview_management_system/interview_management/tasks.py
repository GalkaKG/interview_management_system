from __future__ import absolute_import, unicode_literals
from celery import shared_task
from interview_management_system.interview_management.models import Interview
from django.utils import timezone
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def add(x, y):
    return x + y


@shared_task
def delete_completed_interviews():
    completed_interviews = Interview.objects.filter(status='Completed')

    for interview in completed_interviews:
        interview.delete()

    return f"Deleted {len(completed_interviews)} completed interviews."


@shared_task
def update_interview_statuses():
    logger.info("Celery task update_interview_statuses is running")
    current_datetime = timezone.now()
    current_date = current_datetime.date()
    current_time = current_datetime.time()

    hours, minutes, seconds = str(current_time).split(":")
    current_hour = int(hours) + 3
    current_minutes = int(minutes)

    scheduled_interviews = Interview.objects.filter(status='Scheduled')
    in_progress_interviews = Interview.objects.filter(status='InProgress')

    for interview in scheduled_interviews:
        hour_interview, minutes_interview, sec_interview = str(interview.time).split(":")
        hour_interview = int(hour_interview)
        minutes_interview = int(minutes_interview)

        if hour_interview <= current_hour and minutes_interview <= current_minutes and interview.date <= current_date:
            interview.status = 'InProgress'
            interview.save()

    for interview in in_progress_interviews:
        hour_interview, minutes_interview, sec_interview = str(interview.time).split(":")
        hour_interview = int(hour_interview)
        minutes_interview = int(minutes_interview)

        if hour_interview <= current_hour and minutes_interview + 10 <= current_minutes and interview.date <= current_date:
            interview.status = 'Completed'
            interview.save()

    logger.info("Celery task update_interview_statuses finished")

# @shared_task
