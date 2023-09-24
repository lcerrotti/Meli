from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Project, Task, Inventario, Items
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject, InventarioForm, ItemsForm, InventarioFormWithoutItem

#DATETIME

from datetime import datetime

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


def inventory(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            inv_completo = Inventario.objects.all()
            return render(request, 'inventario.html',{
                'inventario':inv_completo
            })

        


def edit_item(request, item_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            eitem = get_object_or_404(Inventario, pk=item_id)
            form = InventarioFormWithoutItem(instance=eitem)
            return render(request, 'edit_item.html',{
                'eitem':eitem, 'form':form
            })
        else:
            try:
                eitem = get_object_or_404(Inventario, pk=item_id)
                form = InventarioFormWithoutItem(request.POST, instance=eitem)
                form.save()
                return redirect('inventory')
            except:
                return HttpResponse("No es el item que buscabas editar inicialmente.")
    else:
        return HttpResponse("No iniciaste sesion")    




def remove_duplicate_chars(s):
    # Función para eliminar caracteres duplicados en una cadena
    result = []
    for char in s:
        if char not in result:
            result.append(char)
    return ''.join(result)

def are_strings_equal_ignore_case_and_spaces(s1, s2):
    # Función para comparar cadenas sin considerar mayúsculas/minúsculas, espacios y letras duplicadas
    s1_cleaned = remove_duplicate_chars(s1.lower().replace(" ", ""))
    s2_cleaned = remove_duplicate_chars(s2.lower().replace(" ", ""))
    return s1_cleaned == s2_cleaned

def new_item(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, "new_item.html", {
                'form': ItemsForm()
            })
        elif request.method == 'POST':
            try:
                username = request.user.username
                new_item_name = request.POST["item"]
                
                # Verifica si existe un item similar insensible a mayúsculas/minúsculas
                existing_item = Items.objects.filter(item__iexact=new_item_name).first()
                
                if existing_item:
                    error = "Ya existe un item similar."
                    return render(request, 'new_item.html', {
                        'form': ItemsForm(),
                        'error': error
                    })
                
                # Verifica si existe un item similar sin considerar mayúsculas/minúsculas y espacios
                existing_items = Items.objects.all()
                for item in existing_items:
                    if are_strings_equal_ignore_case_and_spaces(new_item_name, item.item):
                        error = "Ya existe un item similar sin considerar mayúsculas/minúsculas y espacios."
                        return render(request, 'new_item.html', {
                            'form': ItemsForm(),
                            'error': error
                        })
                
                # Si no existe, crea el nuevo item
                new_item = Items.objects.create(item=new_item_name, user=username)
                new_item.save()
                
                return redirect('new_item')  
            except:
                error = "Ha ocurrido un error."
                return render(request, 'new_item.html', {
                    'form': ItemsForm(),
                    'error': error
                })
    else:
        return HttpResponse("No iniciaste sesión")


def add_items(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, "add_items.html",{
                'form':InventarioForm()
            })
        else:
            try:
                form = InventarioForm(request.POST)
                form.save()
                return redirect('add_items')
            except:
                return HttpResponse("Ese item ya existe, puedes editarlo en Inventario.")
    else:    
        return HttpResponse("No iniciaste sesion")
    
def filter_view(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            print(request.GET['filter_view'])
            form = Inventario.objects.filter(item__item__icontains=request.GET['filter_view'])
            return render(request, "inventario.html",{
                'inventario':form
            }) 

def detail_view(request, item_id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            eitem = get_object_or_404(Inventario, pk=item_id)
            return render(request, 'detail_view.html',{
                'detail':eitem,
            })
        else:
            return HttpResponse("Error")
    else:    
        return HttpResponse("No iniciaste sesion.")