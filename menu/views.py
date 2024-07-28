from .models import Menu, Plato, Categoria, Producto
from .serializers import MenuSerializer, PlatoSerializer, CategoriaSerializer, ProductoSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets, status
from rest_framework import generics
from rest_framework.decorators import api_view


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


@api_view(['GET'])
def platos_menu_count(request, pk):
    """Cuenta la cantidad de platos de un menú"""
    try:
        menu = Menu.objects.get(pk=pk)
        cantidad = menu.plato.count()
        return JsonResponse(
            {
                'menu_id': menu.id, 
                'plato_count': cantidad
            },
            safe=False,
            status=200
        )
    except Exception as e:
        return JsonResponse(
            {
                'error': str(e)
            },
            safe=False,
            status=400
        )
