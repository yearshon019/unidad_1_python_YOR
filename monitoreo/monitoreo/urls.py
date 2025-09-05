from django.contrib import admin
from django.urls import path
from dispositivos.views import inicio, dispositivo, crear_dispositivo, editar_dispositivo, eliminar_dispositivo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio,),  # Página principal
    path('dispositivos/', inicio, name='dispositivos'),
    path('dispositivos/<int:dispositivo_id>/', dispositivo, name="dispositivo"),
    path('dispositivos/crear/', crear_dispositivo, name='crear_dispositivo'),

    path('dispositivos/eliminar/<int:dispositivo_id>/', eliminar_dispositivo, name="eliminar_dispositivo"),

    path('dispositivos/editar/<int:dispositivo_id>/', editar_dispositivo, name="editar_dispositivo"),
    ]