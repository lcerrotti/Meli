from django import forms
from .models import Inventario, Items

class CreateNewTask(forms.Form):
    title =  forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label="Descripcion de la tarea", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name =  forms.CharField(label="Titulo de project", max_length=200)


class ItemsForm(forms.Form):
    item = forms.CharField(label="Nuevo Item",max_length=200)

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['item', 'descripcion', 'cantidad', 'categoria']

    item = forms.ModelChoiceField(
        queryset=Items.objects.all(),
        empty_label=None,
        label="Item"
    )

    CATEGORIAS = (
        ("ELECTRONICA", "ELECTRONICA"),
        ("INSUMOS", "INSUMOS"),
        ("SEGURIDAD", "SEGURIDAD"),
        ("TRANSITO", "TRANSITO"),
        ("Sin Categoria", "Sin Categoria")
    )
    categoria = forms.ChoiceField(
        choices=CATEGORIAS,
        label="Categoría"
    )

    descripcion = forms.CharField(max_length=200, label="Descripción")
    cantidad = forms.IntegerField(label="Cantidad")

    