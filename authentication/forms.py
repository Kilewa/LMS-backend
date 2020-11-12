from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from authentication.models import Users

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = Users
        fields = ('email', 'username','password','password2',)