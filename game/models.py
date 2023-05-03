from django.db import models
from datetime import date
import json


class Profesor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    
class Grupo(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='grupos')
    numero = models.IntegerField(unique=True)
    
class Alumno(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='alumnos')
    num_lista = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nivel_actual = models.IntegerField(default=1)
    
class Intentos(models.Model):
    alumno = models.ForeignKey(Alumno, null=False, on_delete=models.CASCADE, related_name='intentos')
    aciertos = models.IntegerField(null=False)
    nivel = models.IntegerField(null=False)
    timestamp = models.DateTimeField(auto_now=True)

class Equivocaciones(models.Model):
    alumno = models.ForeignKey(Alumno, null=False, on_delete=models.CASCADE, related_name='equivocaciones')
    tipo = models.IntegerField(null=False)

class Ajustes(models.Model):
    alumno = models.ForeignKey(Alumno, null=False, on_delete=models.CASCADE)
    volumen = models.IntegerField(null=False)
    dificultad = models.CharField(max_length=1, null=False)
