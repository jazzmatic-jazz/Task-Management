from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    '''
        Custom user using AbstractBaseUser where we use
        email field as the main field for login
        fields are:
        - email
        - first_name
        - last_name
        - created_at
        - is_staff
        - is_active
        - is_deleted
    '''    
    email = models.EmailField(max_length=254, unique=True, blank=False, null=False)    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'

    objects = UserManager()
    

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_tasks')
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=350, null=True, blank=True)
    due_date = models.DateField(auto_now=False, auto_now_add=False, editable=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title