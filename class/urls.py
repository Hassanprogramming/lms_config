from django.urls import path
from .views import *

urlpatterns = [
    path('classes/', ClassesView.as_view(), name="classes"),
]

