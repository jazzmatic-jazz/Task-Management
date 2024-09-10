from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from task.models import User, Tasks
from task.forms import TaskForm
from django.shortcuts import render, get_object_or_404, redirect


@login_required(login_url="/task/login")
def index(request):
    '''
        Homepage where, user can see their tasks
    '''
    user = request.user
    task = Tasks.objects.filter(user=user.id)
    return render(request, 'task/index.html', context={"task": task})


@login_required(login_url="/task/login")
def create_task_view(request):
    '''
        an authenticated user can create new task
    '''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)  
            task.user = request.user 
            task.save() 
            return redirect('home')
    else:
        form = TaskForm()

    return render(request, 'task/create.html', {'form': form})


@login_required(login_url="/task/login")
def update_task_view(request, pk):
    '''
        an authenticated user can update their tasks

    '''
    task = get_object_or_404(Tasks, pk=pk)

    if task.user != request.user:
        messages.error(request, "You are not allowed to update this task.")
        return redirect('home') 
    
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)  
            task.user = request.user 
            task.save() 
            return redirect('home')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/update.html', {'form': form})


@login_required(login_url="/task/login")
def delete_task_view(request, pk):
    '''
        an authenticated user can delete their tasks
    '''
    task = get_object_or_404(Tasks, pk=pk)

    if task.user != request.user:
        messages.error(request, "You are not allowed to delete this task.")
        return redirect('home')
    
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'task/delete.html', {'task': task})