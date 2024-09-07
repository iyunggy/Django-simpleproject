from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'email', 'first_name', 'last_name', 'phone', 'password'
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser'
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields':(
                'email', 'first_name', 'last_name', 'phone', 'password1', 'password2',
            )
        }),
    )
    list_display = ['created_at', 'first_name', 'last_name', 'phone']
    search_fields = ['first_name', 'last_name', 'phone']
    ordering = ['-created_at']

admin.site.register(models.User, UserAdmin)
