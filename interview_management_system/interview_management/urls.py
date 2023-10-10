from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MyApiView

router = DefaultRouter()
router.register(r'interviews', views.InterviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/', MyApiView.as_view(), name="endpoint")
]



