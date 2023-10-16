# handlers.py
from django.dispatch import receiver
from interview_management_system.interview_management.signals import interview_updated
from interview_management_system.interview_management.views import send_notification


@receiver(interview_updated)
def handle_interview_updated(sender, **kwargs):
    # Here, you can determine the message you want to send
    message = "Interview has been updated."

    # Call the send_notification function to send this message
    send_notification(message)
