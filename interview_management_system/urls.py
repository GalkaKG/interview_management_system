from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', include('interview_management_system.auth_app.urls')),
    path('', include('interview_management_system.interview_management.urls')),
    path('', include('interview_management_system.api.urls')),
]
