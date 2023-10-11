from django.shortcuts import render, redirect

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .forms import AddCandidateForm, InterviewForm
from .models import Interview, Candidate
from .serializers import InterviewSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class MyApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass


def add_candidate(request):
    if request.method == 'POST':
        form = AddCandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('candidate list')

    else:
        form = AddCandidateForm()
    context = {
        "form": form
    }
    return render(request, "interview-management/add-candidate.html", context)


def candidate_list(request):
    candidates = Candidate.objects.all()
    context = {
        'candidates': candidates
    }
    return render(request, 'interview-management/candidates-list.html', context)


def add_interview(request):
    if request.method == 'POST':
        form = InterviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interview_list')
    else:
        form = InterviewForm()

    return render(request, 'interview-management/add-interview.html', {'form': form})
















# from confluent_kafka import Producer
#
# # Kafka configuration
# kafka_server = 'localhost:9092'
# kafka_topic = 'my_topic'
#
# # Create a Kafka producer
# producer = Producer({'bootstrap.servers': kafka_server})
#
# # Function to send a message to Kafka
# def send_kafka_message(message):
#     producer.produce(kafka_topic, key=None, value=message)
#     producer.flush()
#
# # Example usage in a Django view
# def interview_scheduled(request):
#     # ... logic to schedule an interview ...
#
#     # Send a Kafka message
#     message = {'event': 'interview_scheduled', 'interview_id': interview.id}
#     send_kafka_message(message)
#
#     # ... other view logic ...

