from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from departments.models import Employee

class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = "__all__"