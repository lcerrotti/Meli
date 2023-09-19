from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('hello/', views.hello, name="hello"),
    path('about/', views.about, name="about"),
    path('username/<str:username>', views.username, name="username"),
    path('project/', views.project, name="projects"),
    path('task/', views.task,name="task"),
    path('create_task/', views.create_task,name="Create_task"),
    path('create_project/', views.create_project,name="Create_project"),
]