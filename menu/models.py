from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    descripcion = models.CharField(max_length=250)
    fechaInicio = models.DateTimeField()
    fechaFinal = models.DateTimeField()
    plato = models.ManyToManyField(Plato, blank=True)

    def __str__(self):
        return self.descripcion


class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades'
    KG = 'kg', 'Kilogramos'
    Q = 'q', 'Cuartilla'
    A = 'a', 'Arroba'


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    plato = models.ManyToManyField(Plato, blank=True)
    description = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    unidades = models.CharField(
        max_length=2,
        choices=ProductUnits.choices,
        default=ProductUnits.UNITS
    )

    def __str__(self):
        return self.nombre
