from django.shortcuts import render, redirect
from .models import SalesOrder
from .forms import TaskForm
from .models import Task


def index(request):
    task = Task.objects.order_by('id')
    return render(request, 'main/index.html', {'tasks': task})


def about(request):
    sale = SalesOrder.objects.all()
    return render(request, 'main/about.html', {'about_s': sale})


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect == 'home'
        else:
            error = 'Form is not valid'
    form = TaskForm
    contex = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', contex)

# 'title': 'Main page'?