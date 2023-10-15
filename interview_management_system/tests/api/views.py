from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from interview_management_system.interview_management.models import Candidate, Interview


class CandidatesListViewTests(APITestCase):
    def setUp(self):
        self.candidate1 = Candidate.objects.create(first_name="John", last_name="Doe", email="john@example.com")
        self.candidate2 = Candidate.objects.create(first_name="Jane", last_name="Smith", email="jane@example.com")

    def test_candidates_list(self):
        url = reverse('api candidates')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class CandidateDetailsViewTests(APITestCase):
    def setUp(self):
        self.candidate = Candidate.objects.create(first_name="John", last_name="Doe", email="john@example.com")

    def test_get_candidate(self):
        url = reverse('candidate details', args=[self.candidate.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class EditCandidateViewTests(APITestCase):
    def setUp(self):
        self.candidate = Candidate.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            phone_number="123-456-7890"
        )

    def test_edit_candidate(self):
        url = reverse('edit candidate', args=[self.candidate.pk])
        updated_data = {
            "first_name": "Updated John",
            "last_name": "Updated Doe",
            "email": "updated@example.com",
            "phone_number": "987-654-3210"
        }

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_candidate = Candidate.objects.get(pk=self.candidate.pk)
        self.assertEqual(updated_candidate.first_name, "Updated John")
        self.assertEqual(updated_candidate.last_name, "Updated Doe")
        self.assertEqual(updated_candidate.email, "updated@example.com")
        self.assertEqual(updated_candidate.phone_number, "987-654-3210")


class DeleteCandidateViewTests(APITestCase):
    def setUp(self):
        # Create a sample candidate for testing
        self.candidate = Candidate.objects.create(
            first_name="John",
            last_name="Doe",
            email="john@example.com"
        )

    def test_delete_candidate(self):
        url = reverse('delete candidate', args=[self.candidate.pk])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Candidate.DoesNotExist):
            deleted_candidate = Candidate.objects.get(pk=self.candidate.pk)
