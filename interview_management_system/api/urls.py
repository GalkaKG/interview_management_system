from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from . import views


urlpatterns = (
    path('candidates/', views.candidates_list, name="api candidates"),
    path('candidates/<int:pk>/', views.candidate_details, name="candidate details"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path('schema/docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="docs"),
)

urlpatterns = format_suffix_patterns(urlpatterns)
