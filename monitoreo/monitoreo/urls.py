from django.contrib import admin
from django.urls import path
from dispositivos.views import inicio, panel_dispositivos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio,),  # Página principal
    path('panel/', panel_dispositivos),  # Panel de dispositivos
]
