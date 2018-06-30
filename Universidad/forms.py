from django.forms import ModelForm
from Universidad.models import Profesor, Alumno


class ProfesorForm(ModelForm):
	class Meta:
		model = Profesor
		fields = ['rut', 'nombre', 'apellido', 'edad', 'email', 'direccion', 'telefono', 'imagen']

class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		fields = ['rut', 'nombre', 'apellido', 'edad', 'email', 'direccion', 'telefono', 'imagen']
