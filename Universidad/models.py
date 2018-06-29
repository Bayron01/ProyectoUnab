from django.db import models

# Create your models here.

class Profesor(models.Model):
	rut = models.CharField(max_length=10, help_text="Ej: 18564854-5")
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	edad = models.PositiveIntegerField()
	email = models.EmailField()
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9, help_text="Ej: 962458090")
	imagen = models.ImageField(upload_to='profesor')
	



class Curso(models.Model):
	id_curso = models.PositiveIntegerField()
	nombre = models.CharField(max_length=20)
	fecha_inicio = models.DateField()
	fecha_termino = models.DateField()
	cupos = models.PositiveIntegerField()

class Alumno(models.Model):
	rut = models.CharField(max_length=10, help_text="Ej: 18564854-5")
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	edad = models.PositiveIntegerField()
	email = models.EmailField()
	direccion = models.CharField(max_length=100)
	telefono = models.CharField(max_length=9, help_text="Ej: 962458090")
	imagen = models.ImageField(upload_to='alumno')
	
