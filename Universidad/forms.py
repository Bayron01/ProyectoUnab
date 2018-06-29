from django.forms import ModelForm
from Universidad.models import Profesor


class ProfesorForm(ModelForm):
	class Meta:
		model = Profesor
		fields = ['rut', 'nombre', 'apellido', 'edad', 'email', 'direccion', 'telefono', 'imagen']
