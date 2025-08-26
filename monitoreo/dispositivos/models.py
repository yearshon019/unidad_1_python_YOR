from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Dispositivo(models.Model):
    nombre = models.CharField(max_length=100)
    consumo_maximo = models.IntegerField()
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)
    zona = models.ForeignKey('Zona', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nombre
    
class Zona(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre
    
class Medicion(models.Model):
    fecha = models.DateTimeField()
    consumo_registrado = models.IntegerField()
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Medicion del dispositivo {self.dispositivo} el la fecha {self.fecha} con consumo de {self.consumo_registrado}"
    
class Alerta(models.Model):
    mensaje = models.CharField(max_length=250)
    nivel_alerta = models.CharField(max_length=50)
    fecha = models.DateTimeField(auto_now_add=True)
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Alerta: {self.mensaje} - nivel de alerta: {self.nivel_alerta} - dispositivo: {self.dispositivo} - fecha: {self.fecha}"