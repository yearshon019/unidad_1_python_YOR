from django.contrib import admin

# Register your models here.
from .models import Categoria, Zona, Dispositivo, Alerta, Medicion

admin.site.register([Categoria, Zona, Alerta, Medicion])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'consumo_maximo', 'estado', 'categoria', 'zona')