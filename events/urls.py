from django.contrib import admin
from django.urls import path
from events import views

app_name = 'events'

urlpatterns = [
    path('', views.register_event, name='register_event'),
    path('success/', views.registration_success, name='registration_success'),   
    ]
