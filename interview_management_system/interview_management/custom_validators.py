from django.core.exceptions import ValidationError
from django.utils import timezone


def future_date_validator(date):
    current_date = timezone.now().date()

    if date < current_date:
        raise ValidationError("Interview date must be in the future.")


def future_time_validator(time):
    current_time = timezone.now().time()

    if time <= current_time:
        raise ValidationError("Interview time must be in the future.")
