from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from rest_framework import permissions
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Project",
      default_version='v1',
      description="Documentación rutas para manejo de menues, platos, productos y listas de compra",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
if settings.DEBUG:
    urlpatterns += [
        path(
            'swagger<format>/', 
            schema_view.without_ui(cache_timeout=0), 
            name='schema-json'
            ),
        path(
            'swagger/', 
            schema_view.with_ui('swagger', cache_timeout=0), 
            name='schema-swagger-ui'
            ),
        path(
            'redoc/', 
            schema_view.with_ui('redoc', cache_timeout=0), 
            name='schema-redoc'
            ),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
