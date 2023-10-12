from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from interview_management_system.api.serializers import CandidatesSerializer
from interview_management_system.interview_management.models import Candidate


@api_view(['GET', 'POST'])
def candidates_list(request):

    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidatesSerializer(candidates, many=True)
        return JsonResponse({"candidates": serializer.data})

    if request.method == 'POST':
        serializer = CandidatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)