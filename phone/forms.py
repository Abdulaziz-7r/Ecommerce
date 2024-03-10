from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "password1": forms.TextInput(attrs={"class": "form-control"}),
            "password2": forms.TextInput(attrs={"class": "form-control"}),
        }


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control form-control-sm"}
            ),
            "password": forms.TextInput(attrs={"class": "form-control"}),
        }
