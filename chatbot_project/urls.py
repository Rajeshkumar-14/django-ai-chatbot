from django.contrib import admin
from django.urls import path, include

__project_by__ = "RajeshKumar"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("chatbot.urls")),
]
