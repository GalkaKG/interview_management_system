from django.urls import path
from . import views


urlpatterns = (
    path('candidates/', views.candidates_list, name="api candidates"),
)
