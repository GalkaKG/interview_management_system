from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from interview_management_system.api.custom_functions import get_candidate
from interview_management_system.api.serializers import CandidatesSerializer, InterviewSerializer, \
    FeedbackInterviewSerializer
from interview_management_system.interview_management.models import Candidate, Interview, FeedbackInterview


@extend_schema(responses=CandidatesSerializer)
@api_view(['GET'])
def candidates_list(request, format=None):
    """
    List candidates.

    List all candidates.

    Note:
    - For listing all candidates, send a GET request.

    Responses:
    - 400 Bad Request: Invalid input data.

    """
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidatesSerializer(candidates, many=True)
        return Response(serializer.data)


@extend_schema(responses=CandidatesSerializer)
@api_view(['GET', 'PUT'])
def candidate_details(request, pk, format=None):
    """
        Retrieve a candidate by specifying the candidate's ID.

        Example URL for a specific candidate:
        /candidates/1/

        Responses:
        - 200 OK: Candidate retrieved successfully.
        - 400 Bad Request: Invalid input data.
        - 404 Not Found: Candidate not found.

        """

    candidate = get_candidate(pk)

    if request.method == 'GET':
        serializer = CandidatesSerializer(candidate)
        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@extend_schema(responses=CandidatesSerializer)
@api_view(['PUT'])
def edit_candidate(request, pk, format=None):
    """
        Update a candidate by specifying the candidate's ID.

        Example URL for a specific candidate:
        /edit-candidate/1/

        Example PUT data for updating a candidate:
        {
            "first_name": "Updated John",
            "last_name": "Updated Doe",
            "email": "updated@example.com",
            "phone_number": "987-654-3210"
        }

        Responses:
        - 200 OK: Updated successfully.
        - 400 Bad Request: Invalid input data.
        - 404 Not Found: Candidate not found.

        """

    candidate = get_candidate(pk)

    if request.method == 'PUT':
        serializer = CandidatesSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@extend_schema(responses=CandidatesSerializer)
@api_view(['DELETE'])
def delete_candidate(request, pk, format=None):
    """
        Delete a candidate by specifying the candidate's ID.

        Example URL for a specific candidate:
        /delete-candidate/1/

        Responses:
        - 204 No Content: Candidate deleted successfully.
        - 400 Bad Request: Invalid input data.
        - 404 Not Found: Candidate not found.

    """

    candidate = get_candidate(pk)

    if request.method == 'DELETE':
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@extend_schema(responses=InterviewSerializer)
@api_view(['GET'])
def list_all_interviews(request, format=None):
    """
        List all interviews.

        This view returns a list of all interviews in the system.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: A JSON response containing the serialized list of interviews.

        HTTP Methods:
        - GET: Retrieve a list of all interviews.
    """
    if request.method == 'GET':
        candidates = Interview.objects.all()
        serializer = InterviewSerializer(candidates, many=True)
        return Response(serializer.data)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@extend_schema(responses=InterviewSerializer)
@api_view(['POST'])
def create_interview(request, format=None):
    """
        Create a new interview.

        This endpoint allows you to create a new interview by providing the necessary data in the request body.

        Args:
            request: The HTTP request object.

        Returns:
            Response: An HTTP response indicating the status of the request.

        Example:
            POST /api/create-interview/
            {
                "job": "developer",  # Choose from ['developer', 'designer', 'manager', 'analyst', 'engineer']
                "date": "2023-10-17",  
                "time": "10:00:00",   
                "status": "Scheduled",
                "candidate": 2,
                "interviewer": 2
            }
    """
    if request.method == 'POST':
        serializer = InterviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@extend_schema(responses=InterviewSerializer)
@api_view(['PATCH'])
def update_interview_status(request, pk, format=None):
    """
        Update the status of an interview.

        This view allows updating the status of a specific interview identified by its primary key (pk).

        Parameters:
        - request: The HTTP request object.
        - pk: The primary key of the interview to be updated.

        Returns:
        - Response: A JSON response containing the serialized updated interview.

        HTTP Methods:
        - PATCH: Update the status of the interview.

        Status Choices:
        - 'Scheduled': The interview is scheduled.
        - 'InProgress': The interview is in progress.
        - 'Completed': The interview is completed.
        - 'Canceled': The interview is canceled.

        Example Request:
        ```
        PUT /api/interviews/{pk}/update_status/
        {
            "status": "Completed"
        }
        ```

        Example Response:
        ```
        {
            "id": {interview_id},
            "candidate": {candidate_id},
            "interviewer": {interviewer_id},
            "date": "2023-10-12",
            "time": "14:30:00",
            "status": "Completed"
        }
        ```
        """
    try:
        interview = Interview.objects.get(pk=pk)
    except Interview.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = InterviewSerializer(interview, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(responses=FeedbackInterviewSerializer)
@api_view(['GET'])
def generating_reports(request, format=None):
    """
        Generate and retrieve feedback reports for interviews.

        This view allows generating and retrieving feedback reports for interviews. It returns a list of feedback reports
        associated with interviews.

        Parameters:
        - request: The HTTP request object.

        Returns:
        - Response: A JSON response containing a list of serialized feedback reports.

        HTTP Methods:
        - GET: Retrieve the list of feedback reports for interviews.

        Example Request:
        ```
        GET /api/generating_reports/
        ```

        Example Response:
        ```
        [
            {
                "id": {report_id},
                "interview": {interview_id},
                "interviewer": {interviewer_id},
                "feedback_text": "Positive feedback for the interview.",
                "rating": 5
            },
            {
                "id": {report_id},
                "interview": {interview_id},
                "interviewer": {interviewer_id},
                "feedback_text": "Improvement needed in communication skills.",
                "rating": 3
            }
        ]
        ```
    """
    if request.method == 'GET':
        feedbacks = FeedbackInterview.objects.all()
        serializer = FeedbackInterviewSerializer(feedbacks, many=True)
        return Response(serializer.data)
