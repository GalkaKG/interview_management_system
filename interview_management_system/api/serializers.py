from rest_framework import serializers

from interview_management_system.interview_management.models import Candidate


class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']
