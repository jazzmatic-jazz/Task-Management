from django.contrib import admin
from .models import User, Tasks


class UserAdmin(admin.ModelAdmin):
    fields = ['email', 'first_name', 'is_active', 'is_staff']
    list_display = ['email', 'first_name', 'is_active', 'is_staff']


class TasksAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'due_date', 'is_completed']


admin.site.register(User, UserAdmin)
admin.site.register(Tasks, TasksAdmin)