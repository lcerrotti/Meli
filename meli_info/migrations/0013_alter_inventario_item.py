# Generated by Django 4.2.5 on 2023-09-23 05:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meli_info', '0012_alter_inventario_item_alter_inventario_ultima_mod_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meli_info.items'),
        ),
    ]
