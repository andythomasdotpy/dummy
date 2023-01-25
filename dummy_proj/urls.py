from decouple import config

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("app_1.urls")),
    path(config("URL_ADMIN_PATH"), admin.site.urls),
]