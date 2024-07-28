from django.contrib import admin
from .models import Categoria, Menu, Producto, Plato


admin.site.register(Menu)
admin.site.register(Plato)
admin.site.register(Producto)
admin.site.register(Categoria)
