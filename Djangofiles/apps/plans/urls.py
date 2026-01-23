from django.urls import path
from .views import plan_list, plan_add, plan_edit, plan_delete, upload_feature_icon

urlpatterns = [
    path('', plan_list, name='plan_list'),
    path('add/', plan_add, name='plan_add'),
    path('edit/<int:pk>/', plan_edit, name='plan_edit'),
    path('delete/<int:pk>/', plan_delete, name='plan_delete'),

    # ✅ upload endpoint (NOT under admin)
    path('upload-feature-icon/', upload_feature_icon, name='upload_feature_icon'),
]
