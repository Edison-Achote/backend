from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from .views import (
    PreparacionTerrenoViewSet, SiembraViewSet,
    CuidadoCultivoViewSet, CosechaViewSet,
    PostcosechaViewSet, ProduccionViewSet
)

# Crear un router y registrar nuestros viewsets
router = DefaultRouter()
router.register(r'preparacionterreno', PreparacionTerrenoViewSet)
router.register(r'siembra', SiembraViewSet)
router.register(r'cuidadocultivo', CuidadoCultivoViewSet)
router.register(r'cosecha', CosechaViewSet)
router.register(r'postcosecha', PostcosechaViewSet)
router.register(r'produccion', ProduccionViewSet)

# Las URLs de nuestra API se determinan automáticamente mediante el router.
# Además, incluimos URLs adicionales que pertenecen a nuestra aplicación.
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docapi/', include_docs_urls(title='Procesamiento de Datos de Producción API V1')),
]
