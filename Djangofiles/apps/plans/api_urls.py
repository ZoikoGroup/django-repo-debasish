from django.urls import path
from .api_views import (
    PlanListAPI,
    PlanDetailAPI,
    PlanByCategoryAPI,
)

urlpatterns = [
    path('plans/', PlanListAPI.as_view(), name='plan-list'),
    path('plans/<slug:slug>/', PlanDetailAPI.as_view(), name='plan-detail'),
    path('plans/category/<slug:slug>/', PlanByCategoryAPI.as_view(), name='plan-by-category'),
]
