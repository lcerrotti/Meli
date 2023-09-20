from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index-meli-info"),
    path('project/', views.project, name="projects"),
    path('task/', views.task,name="task"),
    path('create_task/', views.create_task,name="Create_task"),
    path('create_project/', views.create_project,name="Create_project"),
    path('SignUp/', views.sign_up,name="signup"),
    path('LogOut/', views.signout,name="signout"),
    path('SignIn/', views.signin,name="signin"),
    path('navbar/', views.navbar,name="navbar"),
]