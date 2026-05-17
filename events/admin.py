from django.contrib import admin
from .models import EventRegistration

@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ["full_name", "email", "age", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["full_name", "email"]
    readonly_fields = ["created_at"]
