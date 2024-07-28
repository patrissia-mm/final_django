from rest_framework import serializers
from .models import Menu, Plato, Categoria, Producto

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

