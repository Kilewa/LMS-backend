from django.contrib import admin
from .models import Department, Employee
from .forms import EmployeeCreationForm
from django.contrib.auth.admin import UserAdmin

# class CustomEmployeeAdmin(UserAdmin):
#     model = Employee
#     add_form = EmployeeCreationForm

admin.site.register(Department)
admin.site.register(Employee)