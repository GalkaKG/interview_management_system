from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Interview
from .serializers import InterviewSerializer


class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer


class MyApiView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        pass





















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

