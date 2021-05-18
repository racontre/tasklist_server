from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.
#CRUD - create, retrieve, update, delete

def todo_list(request):
    todos = Task.objects.all()
    context = {
        "todolist": todos
    }
    return render(request, "todo/todo-list.html", context)
    

def todo_retrieve (request, id):
    todos = Task.objects.get(id=id)
    context = {
    'todo': todos
    }
    return  render(request, "todo/todo-retrieve.html", context)
    
def todo_create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        due_date = form.cleaned_data['due_date']
        description = form.cleaned_data['description']
        new_task = Task.objects.create(name=name, due_date=due_date, description=description)
        return redirect('/' + str(new_task.id) + '/') #todo redirect to detail
    context = {"form": form}
    return  render(request, "todo/todo-create.html", context)
    
def todo_update(request, id):
    todo = Task.objects.get(id=id)
    form = TaskForm (request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form, 'todo': todo }
    return render(request, "todo/todo-update.html", context)
    
def todo_delete(request, id):
    todo = Task.objects.get(id=id)
    todo.delete() #todo : dont actually deelte
    return render(request, "/")
    