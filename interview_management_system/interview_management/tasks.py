from __future__ import absolute_import, unicode_literals
from datetime import datetime
from celery import shared_task
from interview_management_system.interview_management.models import Interview
from django.utils import timezone
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def delete_completed_interviews():
    completed_interviews = Interview.objects.filter(status='Completed')
    print(completed_interviews)

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
    current_hour = int(hours) - 3
    current_minutes = int(minutes)

    scheduled_interviews = Interview.objects.filter(status='Scheduled')
    in_progress_interviews = Interview.objects.filter(status='InProgress')

    for interview in scheduled_interviews:
        hour_interview, minutes_interview, sec_interview = str(interview.time).split(":")
        hour_interview = int(hour_interview)
        minutes_interview = int(minutes_interview)
        # interview_datetime = datetime.combine(interview.date, interview.time)

        interview.status = 'InProgress'
        interview.save()

        # if hour_interview <= current_hour and minutes_interview <= current_minutes and interview.date <= current_date:
        #     interview.status = 'InProgress'
        #     interview.save()

        # time_until_interview = interview_datetime - current_datetime
        #
        # if time_until_interview.total_seconds() <= 0:
        #     # The scheduled time has come, change status to 'InProgress'
        #     interview.status = 'InProgress'
        #     interview.save()

    # for interview in in_progress_interviews:
    #     interview_datetime = datetime.combine(interview.date, interview.time)
    #     time_until_interview = interview_datetime - current_datetime
    #     if time_until_interview.total_seconds() > 600:  # 10 minutes
    #         # 10 minutes have passed, change status to 'Completed'
    #         interview.status = 'Completed'
    #         interview.save()

    logger.info("Celery task update_interview_statuses finished")


# @shared_task

