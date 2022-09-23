from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm
from django.contrib import messages



def home(request):
    form = TodoForm
    todos = Todo.objects.all()

    context = {
        'todos' : todos,
        "form" : form
    }
    return render(request, "todo/home.html", context)

def todo_create(request):
    
    form = TodoForm

    if request.method == "POST" :
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Todo created successfully")
            return redirect("home")

    context = { ## context ile beraber ilgili template gönderiyoruz! Misal asagida todo_add.html template gönderdik!
        "form" : form
    }

    return render(request, "todo/todo_add.html", context)

def todo_update(request,id): ## update, delete gibi islemler spesifik oldugu icin, id belirtmemiz gerekiyor.
    todo = Todo.objects.get(id=id) ## ilgili id'i databaseden cekiyoruz!
    form = TodoForm(instance=todo) 

    if request.method == "POST" :
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {
        "form" : form
    }

    return render(request, "todo/todo_update.html", context)

def todo_delete(request,id): ## update, delete gibi islemler spesifik oldugu icin, id belirtmemiz gerekiyor.
    todo = Todo.objects.get(id=id) ## ilgili id'i databaseden cekiyoruz!
     

    if request.method == "POST" :
        todo.delete()
        messages.warning(request, "Todo deleted!")
        return redirect("home")

    context = {
        "todo" : todo
    }

    return render(request, "todo/todo_delete.html", context)



    
    
