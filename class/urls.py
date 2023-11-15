from django.urls import path
from .views import *

urlpatterns = [
    path('classes/', ClassesView.as_view(), name="classes"),
    path('classes/<slug:slug>/', CourseDetailView.as_view(), name='course_detail'),
]

