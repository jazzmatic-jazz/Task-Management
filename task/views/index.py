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
        Tasks can be sorted according to
        - completed status
        - due date
    '''
    user = request.user
    task = Tasks.objects.filter(user=user.id)

    if request.method == 'POST':
        get_status = request.POST.get('completed')
        get_sort_by = request.POST.get('sort_by')

        # sorting according to the completed status
        if get_status:
            if get_status == "True":
                task = task.filter(is_completed=True)
            if get_status == "False":
                task = task.filter(is_completed=False)
        
        # sorting acc. to due_date
        if get_sort_by:
            task = task.order_by('due_date')

    return render(request, 'tasks/index.html', context={"task": task})


@login_required(login_url="/task/login")
def create_task_view(request):
    '''
        an authenticated user can create new task
        and that task will be created under the requesting user
        - title
        - description
        - due_date
        - is_completed
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

    return render(request, 'tasks/create.html', {'form': form})


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
    return render(request, 'tasks/update.html', {'form': form})


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
    return render(request, 'tasks/delete.html', {'task': task})

