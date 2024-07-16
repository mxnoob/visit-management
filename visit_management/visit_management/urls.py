from django.contrib import admin
from django.urls import path, include

from visit_management import settings

urlpatterns = [
    path("api/", include("api.urls"), name="api"),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += (path("auth/", include("rest_framework.urls")),)
