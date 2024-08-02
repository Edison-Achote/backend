from rest_framework import viewsets
from .models import PreparacionTerreno, Siembra, CuidadoCultivo, Cosecha, Postcosecha, Produccion
from .serealizer import PreparacionTerrenoSerializer, SiembraSerializer, CuidadoCultivoSerializer, CosechaSerializer, PostcosechaSerializer, ProduccionSerializer

class PreparacionTerrenoViewSet(viewsets.ModelViewSet):
    queryset = PreparacionTerreno.objects.all()
    serializer_class = PreparacionTerrenoSerializer

class SiembraViewSet(viewsets.ModelViewSet):
    queryset = Siembra.objects.all()
    serializer_class = SiembraSerializer

class CuidadoCultivoViewSet(viewsets.ModelViewSet):
    queryset = CuidadoCultivo.objects.all()
    serializer_class = CuidadoCultivoSerializer

class CosechaViewSet(viewsets.ModelViewSet):
    queryset = Cosecha.objects.all()
    serializer_class = CosechaSerializer

class PostcosechaViewSet(viewsets.ModelViewSet):
    queryset = Postcosecha.objects.all()
    serializer_class = PostcosechaSerializer

class ProduccionViewSet(viewsets.ModelViewSet):
    queryset = Produccion.objects.all()
    serializer_class = ProduccionSerializer
