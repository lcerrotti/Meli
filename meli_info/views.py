from django.shortcuts import render
from django.http import HttpResponse
from . models import Project, Task
from django.shortcuts import get_list_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def index(request):
    return render(request, 'index.html')

def hello(request):
    return render(request,"about.html")

def about(request):
    return HttpResponse("ABOUT")

def username(request, username):
    return HttpResponse(f"{username}")

def project(request):
    projects = Project.objects.all()
    return render(request,"projects.html", {
        'projects': projects
    })

def task(request):
    tasks = Task.objects.all()
    return render(request,'task.html',{
        'tasks':tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1)
        return redirect('/meli_info/task/')
       
def create_project(request):
    if request.method == 'GET':
        return render(request, 'create_project.html',{
            'form':CreateNewProject()
        })
    else:
        project = Project.objects.create(name=request.POST['name'])
        return redirect('projects')
       