from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='base/home-page.html'), name='home'),
    path('about', TemplateView.as_view(template_name='base/about.html'), name='about'),
    path('create-job', views.create_job, name="create job"),
    path('add-candidate/', views.add_candidate, name="add candidate"),
    path('candidate-list/', views.candidate_list, name='candidate list'),
    path('add-interview/', views.add_interview, name='add interview'),
    path('interviews/', views.show_interviews, name='interviews list'),
    path('add-feedback/', views.create_feedback, name="add feedback"),
    path('show-feedback/', views.show_feedbacks, name="show feedbacks"),
    path('manage-interviews/<int:pk>/', views.update_interview_status, name='interview update'),
    # path('manage-interviews/', views.interviews_management, name='manage interviews'),
    path('interview/delete/<int:pk>/', views.delete_interview, name='delete interview'),
    path('delete-candidate/<int:pk>/', views.candidate_delete, name='delete candidate'),
]



