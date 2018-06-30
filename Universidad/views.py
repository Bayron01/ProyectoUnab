from django.shortcuts import render
from Universidad.models import Profesor
from Universidad.forms import ProfesorForm



def paginaprincipal(request):
	data = {}
	template_name = 'principal/pagina_principal.html'
	return render(request, template_name, data)

	
def agregarprofesor(request):
    data = {}
    if request.method == "POST":
        data['form'] = ProfesorForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            #return redirect('listar_jugador')

    else:
        data['form'] = ProfesorForm()
   

    template_name = 'profesor/agregar_profesor.html'
    return render(request, template_name, data)





