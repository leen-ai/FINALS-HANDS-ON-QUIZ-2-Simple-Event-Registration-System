from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.register_event, name='home'),  
    ]
