from rest_framework import status
from rest_framework.response import Response
from interview_management_system.interview_management.models import Candidate


def get_candidate(pk):
    try:
        candidate = Candidate.objects.get(pk=pk)
        return candidate
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)