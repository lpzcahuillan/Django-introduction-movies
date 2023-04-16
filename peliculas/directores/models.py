from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField()
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
