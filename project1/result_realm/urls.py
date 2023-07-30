from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.dashboard,name="dashboard"),
    path("Admin",views.Admin,name="Admin"),
    path("persona",views.persona,name="persona"),
    path("exam",views.exam,name="exam"),
    path("result1",views.result1,name="result1"),
    path("downloading",views.downloading,name="downloading"),
    path("dashboard",views.dashboard,name="dashboard"),
]