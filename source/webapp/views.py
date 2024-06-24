from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from webapp.models import Task


def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks/view_task.html", context={"tasks": tasks})

def add_task(request):
    if request.method == 'POST':
        form = Task(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = Task()
    return render(request, 'tasks/add_task.html', {'form': form})

