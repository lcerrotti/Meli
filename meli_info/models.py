from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.title + ' - Del Proyecto: ' + self.project.name


class Items(models.Model):
    item = models.CharField(max_length=200, unique=True)
    user = models.CharField(max_length=200)
    last_item_create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item



class Inventario(models.Model):

    #Opciones

    CATEGORIAS = (
        ("ELECTRONICA", "ELECTRONICA"),
        ("INSUMOS","INSUMOS"),
        ("SEGURIDAD","SEGURIDAD"),
        ("TRANSITO","TRANSITO"),
        ("Sin Categoria","Sin Categoria")
    )

    item = models.OneToOneField(Items, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=60, choices=CATEGORIAS, default="Sin Categoria")
    ultima_mod = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.item)
        

class HistoricoItem(models.Model):

    item = models.CharField(max_length=200)
    modificacion = models.DateTimeField(auto_now=True)
    cantidad = models.IntegerField()
    user = models.CharField(max_length=200)

    def __str__(self):
        return str(self.item)