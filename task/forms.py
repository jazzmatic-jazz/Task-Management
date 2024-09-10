from django import forms
from .models import User, Tasks

class TaskForm(forms.ModelForm):
    '''
        Form for creating a new task or updating an existing 
        task
        - title
        - description
        - due_date
        - is_completed
    '''
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'due_date', 'is_completed']

        