from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='base/home-page.html'), name="home"),
    path('add-candidate/', views.add_candidate, name="add candidate"),
    path('candidate-list/', views.candidate_list, name='candidate list'),
    path('add-interview/', views.add_interview, name='add interview'),
    path('interviews/', views.show_interviews, name='show interviews'),
    path('add-feedback/', views.create_feedback, name="add feedback"),
    path('show-feedback/', views.show_feedbacks, name="show feedbacks"),
]



