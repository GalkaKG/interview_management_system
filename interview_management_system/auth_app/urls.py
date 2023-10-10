from django.contrib.auth.views import LoginView
from django.urls import path

from interview_management_system.auth_app import views


urlpatterns = (
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
)
