from django.urls import path
from .views import JobListAPI

urlpatterns = [
    path('', JobListAPI.as_view()),
]
