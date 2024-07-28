from django.db import models
from .validators import validar_nombre_plato, validar_fechas_menu


class Categoria(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre
    
class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'
    Q = 'q', 'Cuartilla'
    A = 'a', 'Arroba'


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    description = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )

    def __str__(self):
        return self.nombre
    



class Plato(models.Model):
    nombre = models.CharField(max_length=150, validators=[validar_nombre_plato])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through='PlatoProducto')
    def __str__(self):
        return self.nombre

class PlatoProducto(models.Model):
    plato = models.ForeignKey(Plato, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=2, decimal_places=2)
    
class Menu(models.Model):
    descripcion = models.CharField(max_length=250)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    plato = models.ManyToManyField(Plato, blank=True)

    def __str__(self):
        return self.descripcion
    
    def clean(self):
        validar_fechas_menu(self.fechaFinal, self.fechaInicio)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



