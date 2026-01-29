from django.urls import path
from .views import job_list_api
urlpatterns = [
     path('api/', job_list_api, name='job-list-api'),

]
