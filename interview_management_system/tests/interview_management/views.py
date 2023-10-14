from django.test import TestCase
from django.urls import reverse


# ***** Tests for the add_candidate view

class AddCandidateViewTest(TestCase):
    def test_add_candidate_post_valid_form(self):
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
        }

        response = self.client.post(reverse('add candidate'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('candidate list'))

    def test_add_candidate_get_request(self):
        response = self.client.get(reverse('add candidate'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'interview-management/add-candidate.html')

    def test_add_candidate_post_invalid_form(self):
        data = {
            'first_name': '',
            'last_name': 'Doe',
            'email': 'invalid-email',
            'phone_number': '1234567890',
        }

        response = self.client.post(reverse('add candidate'), data)
        self.assertEqual(response.status_code, 200)

        self.assertTrue('form' in response.context)
        form = response.context['form']
        self.assertTrue(form.errors)



