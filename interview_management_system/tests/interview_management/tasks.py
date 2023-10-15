from django.test import TestCase
from django.utils import timezone

from interview_management_system.interview_management.models import Interview, Job
from interview_management_system.interview_management.tasks import delete_completed_interviews


class DeleteCompletedInterviewsTestCase(TestCase):
    def test_delete_completed_interviews(self):
        job = Job.objects.create(title='developer')

        interview = Interview.objects.create(
            candidate_id=2,
            interviewer_id=1,
            job=job,  # Use the Job instance
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
