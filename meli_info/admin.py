from django.contrib import admin
from .models import Project, Task, Inventario,Items, HistoricoItem
# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Inventario)
admin.site.register(Items)
admin.site.register(HistoricoItem)