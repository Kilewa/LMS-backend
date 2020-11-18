from django.contrib import admin
from profiles.models import Profile
from departments.models import Employee, Department


admin.site.register(Department)
admin.site.register(Employee)