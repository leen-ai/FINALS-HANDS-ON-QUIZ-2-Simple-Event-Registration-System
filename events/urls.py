from django.contrib import admin
from django.urls import path, include
from events import views

app_name = 'events'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls', namespace='events')),  
    ]
