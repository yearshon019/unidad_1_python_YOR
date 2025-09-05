from django.shortcuts import render, redirect, get_object_or_404
from .models import Dispositivo
from .forms import DispositivoForm
# Create your views here.

def inicio(request):
    dispositivos = Dispositivo.objects.select_related("categoria")
    return render(request, 'dispositivos/inicio.html', {"dispositivos": dispositivos})

def dispositivo(request, dispositivo_id):
    dispositivo = Dispositivo.objects.get(id=dispositivo_id)
    return render(request, 'dispositivos/dispositivos.html', {"dispositivo": dispositivo})


def crear_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dispositivos')
    else:
        form = DispositivoForm()
    return render(request, 'dispositivos/crear_dispositivo.html', {'form': form})


def editar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        form = DispositivoForm(request.POST, instance=dispositivo)
        if form.is_valid():
            form.save()
            return redirect('dispositivos')
    else:
        form = DispositivoForm(instance=dispositivo)
    return render(request, 'dispositivos/editar_dispositivo.html', {'form': form})

def eliminar_dispositivo(request, dispositivo_id):
    dispositivo = get_object_or_404(Dispositivo, id=dispositivo_id)
    if request.method == 'POST':
        dispositivo.delete()
        return redirect('dispositivos')
    return render(request, 'dispositivos/eliminar_dispositivo.html', {'dispositivo': dispositivo})