from django.test import TestCase
from django.utils import timezone

from interview_management_system.interview_management.models import Interview
from interview_management_system.interview_management.tasks import delete_completed_interviews


# ***** Unit tests for the delete_completed_interviews task

class DeleteCompletedInterviewsTestCase(TestCase):
    def test_delete_completed_interviews(self):
        interview = Interview.objects.create(
            candidate_id=2,
            interviewer_id=1,
            job='developer',
            date=timezone.now().date(),
            time=timezone.now().time(),
            status='Completed',
        )

        self.assertEqual(Interview.objects.filter(status='Completed').count(), 1)

        result = delete_completed_interviews()

        self.assertIn('Deleted 1 completed interviews', result)
        self.assertEqual(Interview.objects.filter(status='Completed').count(), 0)

    def test_no_completed_interviews(self):
        self.assertEqual(Interview.objects.filter(status='Completed').count(), 0)

        result = delete_completed_interviews()

        self.assertIn('Deleted 0 completed interviews', result)
