from .models import Menu, Plato, Categoria, Producto
from .serializers import MenuSerializer, PlatoSerializer, CategoriaSerializer, ProductoSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer

class CategoriaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer