# Generated by Django 5.0.7 on 2024-07-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_plato_menu_alter_producto_plato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plato',
            name='menu',
        ),
        migrations.AddField(
            model_name='menu',
            name='plato',
            field=models.ManyToManyField(blank=True, to='menu.plato'),
        ),
    ]
