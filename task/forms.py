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
    description = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Tasks
        fields = ['title', 'description', 'due_date', 'is_completed']

        