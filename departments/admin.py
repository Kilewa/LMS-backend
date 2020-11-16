from django.contrib import admin

from .models import Department, Employee
from django.contrib.auth.admin import UserAdmin



class DepartmentAdmin(UserAdmin):
    
    model = Department
    list_display = ('name','code','dept_head',)
    list_filter = ('name','code')
    fieldsets = (
        (None, {'fields': ('name','code','dept_head')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','code','dept_head')}
        ),
    )
    search_fields = ('code',)
    ordering = ('name',)


admin.site.register(Department)
admin.site.register(Employee)