from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EventRegistrationForm
from .models import EventRegistration

def register_event(request):
    if request.method == "POST":
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save()
            request.session["last_registration_id"] = registration.id
            return redirect("events:registration_success")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = EventRegistrationForm()

    return render(request, "events/register.html", {"form": form})


def registration_success(request):
    registration_id = request.session.get("last_registration_id")
    registration = None

    if registration_id:
        try:
            registration = EventRegistration.objects.get(id=registration_id)
        except EventRegistration.DoesNotExist:
            pass

    return render(request, "events/success.html", {"registration": registration})
