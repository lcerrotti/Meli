from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Project, Task
from django.shortcuts import get_list_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

#CRUD
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request, 'index.html')

def navbar(request):
    return render(request, 'navbar.html')


def project(request):
    if request.user.is_authenticated:
        username =  request.user.username
        projects = Project.objects.filter(user=username)
        return render(request,"projects.html", {
            'projects': projects
        })
    else:
        return HttpResponse("No iniciaste sesion")

def task(request):
    if request.user.is_authenticated:
        username= request.user.username
        tasks = Task.objects.filter(user=username)
        return render(request,'task.html',{
            'tasks':tasks
        })
    else:
        return HttpResponse("No iniciaste sesion")

def create_task(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'create_task.html',{
                'form':CreateNewTask()
            })
        else:
            if request.user.is_authenticated:
                username = request.user.username
                Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=1, user=username)
                return redirect('/meli_info/task/')
    else:
        return HttpResponse("No iniciaste sesion")
       
def create_project(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'create_project.html',{
                'form':CreateNewProject()
            })
        else:
            project = Project.objects.create(name=request.POST['name'])
            return redirect('projects')
    else:
        return HttpResponse("No iniciaste sesion")
    
    
def sign_up(request):
    if request.method == 'GET':
         return render(request, 'signup.html',{
            'form':UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(task)
            except:
                 return render(request, 'signup.html',{
                    'form':UserCreationForm,
                    'error':"El usuario ya existe"
                    })
        return render(request, 'signup.html',{
                        'form':UserCreationForm,
                        'error':"Las contraseñas no coinciden"
                        })
    

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':

        return render(request, 'signin.html',{
            'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',{
            'form':AuthenticationForm,
            'error':"Username or password not match"
            })
        else:
            login(request, user)
            return redirect(task)
