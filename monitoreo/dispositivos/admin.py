from django.contrib import admin

# Register your models here.
from .models import Categoria, Zona, Dispositivo

admin.site.register([Categoria, Zona])

@admin.register(Dispositivo)
class DispositivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'consumo_maximo', 'estado', 'categoria', 'zona')