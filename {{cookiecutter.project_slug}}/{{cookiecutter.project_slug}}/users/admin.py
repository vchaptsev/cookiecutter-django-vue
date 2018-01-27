from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm

    fieldsets = [
        ['Auth', {'fields': ['email', 'password']}],
        ['Personal info', {'fields': ['last_name', 'first_name', 'middle_name', 'avatar', 'phone', 'address']}],
        ['Settings', {'fields': ['groups', 'is_admin', 'is_active', 'is_staff', 'is_superuser']}],
        ['Important dates', {'fields': ['last_login', 'registered_at']}],
    ]
    add_fieldsets = [
        [None, {'classes': ['wide'], 'fields': ['email', 'password']}],
    ]
    list_display = ['full_name', 'email']
    readonly_fields = ['last_login', 'registered_at']
    ordering = ['email']
