from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "service": "Golite Backend",
        "status": "running",
        "version": "v1"
    })

urlpatterns = [
    path("", home),  #  ROOT URL
    path("admin/", admin.site.urls),
    path("plans/", include("apps.plans.urls")),
  path('api/v1/', include('apps.plans.api_urls')),
    path("api/v1/", include("apps.accounts.urls")),
    path("api/v1/", include("apps.coupons.urls")),
    path('jobs/', include('apps.jobs.urls')),
]
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
