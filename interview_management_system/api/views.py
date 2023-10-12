from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from interview_management_system.api.serializers import CandidatesSerializer
from interview_management_system.interview_management.models import Candidate


@api_view(['GET', 'POST'])
def candidates_list(request, format=None):
    """
    List and create candidates.

    List all candidates or create a new candidate.

    Note:
    - For listing all candidates, send a GET request.
    - For creating a new candidate, send a POST request with candidate details.

    Example POST data for creating a candidate:
    {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone_number": "123-456-7890"
    }

    Responses:
    - 201 Created: Candidate created successfully.
    - 400 Bad Request: Invalid input data.

    """
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidatesSerializer(candidates, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CandidatesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def candidate_details(request, pk, format=None):
    """
        Retrieve, update, or delete a candidate by ID.

        Retrieve, update, or delete a candidate by specifying the candidate's ID.

        Example URL for a specific candidate:
        /candidates/1/

        Example PUT data for updating a candidate:
        {
            "first_name": "Updated John",
            "last_name": "Updated Doe",
            "email": "updated@example.com",
            "phone_number": "987-654-3210"
        }

        Responses:
        - 200 OK: Candidate retrieved or updated successfully.
        - 204 No Content: Candidate deleted successfully.
        - 400 Bad Request: Invalid input data.
        - 404 Not Found: Candidate not found.

        """
    try:
        candidate = Candidate.objects.get(pk=pk)
    except Candidate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CandidatesSerializer(candidate)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CandidatesSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
