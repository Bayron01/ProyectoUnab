from django.forms import ModelForm
from Universidad.models import Profesor, Alumno, Curso


class ProfesorForm(ModelForm):
	class Meta:
		model = Profesor
		fields = ['rut', 'nombre', 'apellido', 'edad', 'email', 'direccion', 'telefono', 'imagen']

class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		fields = ['rut', 'nombre', 'apellido', 'edad', 'email', 'direccion', 'telefono', 'imagen']

class CursoForm(ModelForm):
	class Meta:
		model = Curso
		fields = ['id_curso', 'nombre', 'fecha_inicio', 'fecha_termino', 'cupos']