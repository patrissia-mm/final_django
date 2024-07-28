from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'plato', views.PlatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categorias/', views.CategoriaCreateView.as_view()),
    path('productos/', views.ProductoCreateView.as_view()),
    path('menu/<int:pk>/platos_menu/', views.platos_menu_count),
]