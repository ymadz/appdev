from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from datetime import date

# Automatically set the status before saving a task
def set_task_status(task):
    today = date.today()
    if task.due_date < today:
        task.status = 'Overdue'
    elif task.due_date == today:
        task.status = 'Due Today'
    else:
        task.status = 'Upcoming'
    return task

# Show all tasks
from django.shortcuts import render
from .models import Task

def task_list(request):
    query = request.GET.get('q')
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else:
        tasks = Task.objects.all()
    
    return render(request, 'task_list.html', {'tasks': tasks})

# Add new task
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task = set_task_status(task)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})

# Edit existing task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            task = set_task_status(task)
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})

# Delete task (confirmation page)
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
