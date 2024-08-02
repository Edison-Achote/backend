from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Modelo para Preparación del Terreno
class PreparacionTerreno(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField()
    
    def __str__(self):
        return f"Preparación del Terreno del {self.fecha_inicio} al {self.fecha_fin}"

# Modelo para Siembra
class Siembra(models.Model):
    fecha = models.DateField()
    tipo_planta = models.CharField(max_length=200)
    descripcion = models.TextField()
    
    def __str__(self):
        return f"Siembra de {self.tipo_planta} el {self.fecha}"

# Modelo para Cuidado del Cultivo
class CuidadoCultivo(models.Model):
    fecha = models.DateField()
    actividades = models.TextField()
    
    def __str__(self):
        return f"Cuidado del Cultivo el {self.fecha}"

# Modelo para Cosecha
class Cosecha(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cantidad = models.IntegerField()
    
    def __str__(self):
        return f"Cosecha del {self.fecha_inicio} al {self.fecha_fin} - {self.cantidad} unidades"

# Modelo para Postcosecha
class Postcosecha(models.Model):
    fecha = models.DateField()
    actividades = models.TextField()
    
    def __str__(self):
        return f"Postcosecha el {self.fecha}"

# Modelo para registrar cada etapa del proceso de producción
class Produccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    preparacion_terreno = models.ForeignKey(PreparacionTerreno, on_delete=models.CASCADE)
    siembra = models.ForeignKey(Siembra, on_delete=models.CASCADE)
    cuidado_cultivo = models.ForeignKey(CuidadoCultivo, on_delete=models.CASCADE)
    cosecha = models.ForeignKey(Cosecha, on_delete=models.CASCADE)
    postcosecha = models.ForeignKey(Postcosecha, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Producción gestionada por {self.usuario}"
