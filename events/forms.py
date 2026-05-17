from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import EventRegistration

class EventRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        min_length=8,
        help_text="Password must be at least 8 characters long."
    )

    class Meta:
        model = EventRegistration
        fields = ["full_name", "email", "age", "password"]
        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name")
        if len(full_name) < 5:
            raise ValidationError("Full name must be at least 5 characters long.")
        return full_name

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@gmail.com"):
            raise ValidationError("Email must end with @gmail.com.")
        return email

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age < 18:
            raise ValidationError("You must be at least 18 years old to register.")
        return age

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data["password"])
        if commit:
            instance.save()
        return instance
