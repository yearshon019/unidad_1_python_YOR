from django.contrib import admin
from django.urls import path
from dispositivos.views import inicio, dispositivo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio,),  # Página principal
    path('dispositivos/', inicio, name='dispositivos'),
    path('dispositivos/<int:dispositivo_id>/', dispositivo, name="dispositivo")
    ]