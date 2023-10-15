from django.urls import path

from interview_management_system.auth_app import views


urlpatterns = (
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>', views.profile_details, name='profile details'),
    path('edit-profile/', views.ProfileEditView.as_view(), name='profile edit'),
    path('options-logout/', views.option_logout, name='options logout'),
)
