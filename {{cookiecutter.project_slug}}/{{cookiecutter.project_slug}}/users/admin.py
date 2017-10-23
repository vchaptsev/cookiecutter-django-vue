from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm

    fieldsets = [
        [_('Auth'), {'fields': ['email', 'password']}],
        [_('Personal info'), {'fields': ['last_name', 'first_name', 'middle_name', 'avatar', 'phone', 'address']}],
        [_('Settings'), {'fields': ['groups', 'is_admin', 'is_active', 'is_staff', 'is_superuser']}],
        [_('Important dates'), {'fields': ['last_login', 'registered_at']}],
    ]
    add_fieldsets = [
        [None, {'classes': ['wide'], 'fields': ['email', 'password']}],
    ]
    list_display = ['full_name', 'email']
    readonly_fields = ['last_login', 'registered_at']
    ordering = ['email']
