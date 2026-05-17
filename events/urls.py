from django.contrib import admin
from django.urls import path, include
from events import views

app_name = 'events'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('success/', views.registration_success, name='registration_success'),  
    path('', views.register_event, name='home'), 
    ]
