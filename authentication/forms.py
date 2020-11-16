from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from authentication.models import User

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"