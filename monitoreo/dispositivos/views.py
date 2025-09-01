from django.shortcuts import render
from django.http import HttpResponse
from .models import Dispositivo
# Create your views here.

def inicio(request):
    dispositivos = Dispositivo.objects.select_related("categoria")
    return render(request, 'dispositivos/inicio.html', {"dispositivos": dispositivos})

def dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)
    return render(request, 'dispositivos/dispositivos.html', {"dispositivo": dispositivo})