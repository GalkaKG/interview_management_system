from rest_framework import serializers

from interview_management_system.interview_management.models import Candidate, Interview, FeedbackInterview


class CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']


class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = '__all__'


class FeedbackInterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackInterview
        fields = '__all__'
