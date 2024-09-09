from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'first_name', 'is_active', 'is_staff']
    list_display = ['email', 'first_name', 'is_active', 'is_staff']


admin.site.register(User, UserAdmin)