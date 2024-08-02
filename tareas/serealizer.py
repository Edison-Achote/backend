from rest_framework import serializers
from .models import PreparacionTerreno, Siembra, CuidadoCultivo, Cosecha, Postcosecha, Produccion

class PreparacionTerrenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreparacionTerreno
        fields = '__all__'

class SiembraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Siembra
        fields = '__all__'

class CuidadoCultivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuidadoCultivo
        fields = '__all__'

class CosechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cosecha
        fields = '__all__'

class PostcosechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postcosecha
        fields = '__all__'

class ProduccionSerializer(serializers.ModelSerializer):
    preparacion_terreno = PreparacionTerrenoSerializer()
    siembra = SiembraSerializer()
    cuidado_cultivo = CuidadoCultivoSerializer()
    cosecha = CosechaSerializer()
    postcosecha = PostcosechaSerializer()
    
    class Meta:
        model = Produccion
        fields = '__all__'
