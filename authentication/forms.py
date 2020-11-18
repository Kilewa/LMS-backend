from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth import authenticate
from departments.models import Employee

from authentication.models import User



class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = "__all__"


class EmployeeUpdateForm(UserChangeForm):

    class Meta:
        model = Employee
        fields = "__all__"