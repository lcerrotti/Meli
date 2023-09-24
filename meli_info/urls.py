from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name="index-meli-info"),
    path('project/', views.project, name="projects"),
    path('task/', views.task,name="task"),
    path('create_task/', views.create_task,name="Create_task"),
    path('create_project/', views.create_project,name="Create_project"),
    path('add_items/', views.add_items,name="add_items"),
    path('new_item/', views.new_item,name="new_item"),
    path('inventory/', views.inventory,name="inventory"),
    path('edit_item/<int:item_id>', views.edit_item,name="edit_item"),
    path('detail_view/<int:item_id>', views.detail_view,name="detail_view"),
    path('filter_view/', views.filter_view,name="filter_view"),
    path('SignUp/', views.sign_up,name="signup"),
    path('LogOut/', views.signout,name="signout"),
    path('SignIn/', views.signin,name="signin"),
    path('navbar/', views.navbar,name="navbar"),
]