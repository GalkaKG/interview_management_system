from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('', TemplateView.as_view(template_name='home-page.html'), name="home"),
    path('', include('interview_management_system.auth_app.urls')),
    path('', include('interview_management_system.interview_management.urls')),
]
