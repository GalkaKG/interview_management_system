from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views


urlpatterns = (
    path('candidates/', views.candidates_list, name="api candidates"),
    path('candidates/<int:pk>/', views.candidate_details, name="candidate details"),
    path('edit-candidate/<int:pk>/', views.edit_candidate, name="edit candidate"),
    path('delete-candidate/<int:pk>/', views.delete_candidate, name="delete candidate"),
    path('list-interviews/', views.list_all_interviews, name="list all interviews"),
    path('create-interview/', views.create_interview, name="api create interview"),
    path('update-interview-status/<int:pk>/', views.update_interview_status, name="update interview status"),
    path('generating_reports/', views.generating_reports, name="generating reports"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
)

# urlpatterns = format_suffix_patterns(urlpatterns)
