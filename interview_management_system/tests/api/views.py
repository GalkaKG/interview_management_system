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
        # Create a sample candidate for testing
        self.candidate = Candidate.objects.create(first_name="John", last_name="Doe", email="john@example.com")

    def test_get_candidate(self):
        url = reverse('candidate details', args=[self.candidate.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_candidate(self):
        url = reverse('candidate details', args=[self.candidate.pk])
        updated_data = {
            "first_name": "Updated John",
            "last_name": "Updated Doe",
            "email": "updated@example.com",
            "phone_number": "987-654-3210"
        }

        response = self.client.put(url, updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_candidate(self):
        url = reverse('candidate details', args=[self.candidate.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


