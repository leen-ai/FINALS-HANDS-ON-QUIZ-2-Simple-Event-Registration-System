from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    path("register/", views.register_event, name="register_event"),
    path("success/", views.registration_success, name="registration_success"),
]
