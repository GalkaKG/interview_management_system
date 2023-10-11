from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MyApiView

router = DefaultRouter()
router.register(r'interviews', views.InterviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add-candidate/', views.add_candidate, name="add candidate"),
    path('candidate-list/', views.candidate_list, name='candidate list'),
    path('add-interview/', views.add_interview, name='add interview'),
    path('api/', MyApiView.as_view(), name="endpoint"),
]



