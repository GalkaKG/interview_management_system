from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('interview_management_system.auth_app.urls')),
    path('', include('interview_management_system.interview_management.urls')),
    path('api/', include('interview_management_system.api.urls')),
    path('404/', TemplateView.as_view(template_name='error-pages/error-page.html'), name='error_404'),
]

handler404 = 'interview_management_system.interview_management.views.custom_404'
