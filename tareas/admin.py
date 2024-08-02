from django.contrib import admin
from .models import PreparacionTerreno, Siembra, CuidadoCultivo, Cosecha, Postcosecha, Produccion

admin.site.register(PreparacionTerreno)
admin.site.register(Siembra)
admin.site.register(CuidadoCultivo)
admin.site.register(Cosecha)
admin.site.register(Postcosecha)
admin.site.register(Produccion)
