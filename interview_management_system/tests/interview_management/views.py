from django.test import TestCase
from django.urls import reverse



from django.test import TestCase
from django.urls import reverse

from interview_management_system.interview_management.models import Candidate


class AddCandidateViewTests(TestCase):
    def test_create_candidate(self):
        candidate = Candidate.objects.create(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone_number="1234567890"
        )

        self.assertEqual(candidate.first_name, "John")
        self.assertEqual(candidate.last_name, "Doe")
        self.assertEqual(candidate.email, "john.doe@example.com")
        self.assertEqual(candidate.phone_number, "1234567890")

        retrieved_candidate = Candidate.objects.get(email="john.doe@example.com")
        self.assertEqual(retrieved_candidate, candidate)
