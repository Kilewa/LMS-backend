from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,Departmenthead,Employee


class CustomUserAdmin(UserAdmin):
    
    model = CustomUser
    list_display = ('email','role','first_name','last_name','address','mobile','is_staff','is_verified', 'is_active',)
    list_filter = ('email','role')
    fieldsets = (
        (None, {'fields': ('email','role','first_name','last_name','address','mobile', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','role','first_name','last_name','address','mobile', 'password1', 'password2', 'is_staff', 'is_active','is_verified')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Departmenthead)
admin.site.register(Employee)