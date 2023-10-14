from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from interview_management_system.interview_management.custom_validators import future_date_validator, future_time_validator


class CustomValidatorsTests(TestCase):
    def test_future_date_validator(self):
        # Test a valid future date
        future_date = timezone.now().date() + timezone.timedelta(days=1)
        try:
            future_date_validator(future_date)
        except ValidationError:
            self.fail("future_date_validator raised an error for a valid date.")

        # Test an invalid past date
        past_date = timezone.now().date() - timezone.timedelta(days=1)
        with self.assertRaises(ValidationError):
            future_date_validator(past_date)

    def test_future_time_validator(self):
        # Test a valid future time
        future_time = (timezone.now() + timezone.timedelta(minutes=30)).time()
        try:
            future_time_validator(future_time)
        except ValidationError:
            self.fail("future_time_validator raised an error for a valid time.")

        # Test an invalid past time
        past_time = (timezone.now() - timezone.timedelta(minutes=30)).time()
        with self.assertRaises(ValidationError):
            future_time_validator(past_time)
