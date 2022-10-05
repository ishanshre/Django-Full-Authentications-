from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import get_user_model
# Register your models here.

@admin.register(get_user_model())
class UserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ['username','email','is_staff','is_active']
    fieldsets = UserAdmin.fieldsets + (('Additional Information', {'fields':('date_of_birth','gender',)}),)
    add_fieldsets = UserAdmin.fieldsets + (('Additional Information', {'fields':('date_of_birth', 'gender',)}),)