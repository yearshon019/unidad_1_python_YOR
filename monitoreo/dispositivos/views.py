from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    contexto = {"nombre": "Yearshon Orrego"}
    productos = [
        {"nombre": "Laptop", "precio": 1000},
        {"nombre": "Celular", "precio": 500},
        {"nombre": "Tablet", "precio": 300},
    ]
    
    return render(request, "dispositivos/inicio.html", {
        "contexto": contexto,
        "productos": productos
    })


def panel_dispositivos(request):
    dispositivos = [
        {"nombre": "sensor temperatura", "consumo": 50},
        {"nombre": "sensor luminosidad", "consumo": 120},
        {"nombre": "sensor humedad", "consumo": 40},
        {"nombre": "sensor presion", "consumo": 180},
    ]

    consumo_maximo = 150

    return render(request, "dispositivos/dispositivos.html", {
        "dispositivos": dispositivos,
        "consumo_maximo": consumo_maximo
    })
