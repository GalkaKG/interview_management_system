from __future__ import absolute_import, unicode_literals
import os

from celery import Celery, shared_task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'interview_management_system.settings')

app = Celery('interview_management_system')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")

# app.conf.beat_schedule = {
#     'add': {
#         'task': 'interview_management_system.management_system.tasks.add',
#         'schedule': crontab(minute='0', hour='0'),
#     },
# 'enable-scheduler': {
#     'task': 'celery.beat.Beat',
#     'schedule': timedelta(seconds=10),
# },
# }