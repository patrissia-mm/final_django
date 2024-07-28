from .models import Menu, Plato, Categoria, Producto, PlatoProducto
from .serializers import MenuSerializer, PlatoSerializer, CategoriaSerializer, ProductoSerializer
from django.shortcuts import render, get_object_or_404
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


@api_view(['GET'])
def lista_compras(request, menu_id):
    """Devuelve la lista de compras basada en un menú"""
    try:
        menu = get_object_or_404(Menu, pk=menu_id)
        productos = {}

        for plato in menu.plato.all():
            for platoproducto in PlatoProducto.objects.filter(plato=plato):
                producto = platoproducto.producto
                if producto.id in productos:
                    if producto.id in productos:
                        productos[producto.id]['çantidad'] += platoproducto.cantidad
                    else:
                        productos[producto.id] = {
                            'nombre': producto.nombre,
                            'cantidad': platoproducto.cantidad
                        }

        return JsonResponse(
            {
                "productos": list(productos.values())
            },
            safe=False,
            status=200
        )
    except Menu.DoesNotExist:
        return JsonResponse(
            {
                'error': 'Menu no encontrado'
            },
            status=404
        )
    except Exception as e:
        return JsonResponse(
            {
                'error': str(e)
            },
            safe=False,
            status=400
        )
