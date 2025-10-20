from django.db import models
from django.contrib.auth.models import User


# Modelo que representa una categoría para las solicitudes.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        # Muestra el nombre de la categoría
        return self.nombre

# Modelo que representa una solicitud (ticket) en la mesa de ayuda.
class Solicitud(models.Model):

    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    # choices= para estado y prioridad definen opciones predeterminadas
    estado = models.CharField(choices=[('nueva', 'Nueva'), ('en_progreso', 'En Progreso'), ('cerrada', 'Cerrada')], max_length=50,)
    prioridad = models.CharField(choices=[('low', 'Baja'), ('med', 'Media'), ('high', 'Alta')], max_length=50,)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Muestra el id y el título 
        return f"{self.id} - {self.titulo}"