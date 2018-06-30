from django.shortcuts import render
from django.shortcuts import redirect
from Universidad.models import Profesor, Alumno
from Universidad.forms import ProfesorForm, AlumnoForm



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

            return redirect('listar_profesor')

    else:
        data['form'] = ProfesorForm()
   

    template_name = 'profesor/agregar_profesor.html'
    return render(request, template_name, data)

def listarprofesor(request):
    data = {}
    
    data['object_list'] = Profesor.objects.all().order_by('id')

    template_name = 'profesor/listar_profesor.html'
    return render(request, template_name, data)

def detallarprofesor(request, profesor_id):
    data = {}
    data['profesor'] = Profesor.objects.get(pk=profesor_id)
    template_name = 'profesor/detallar_profesor.html'
    return render(request, template_name, data)

def editarprofesor(request, profesor_id):
    data = {}
    profesor = Profesor.objects.get(pk=profesor_id)
    if request.method == "GET":
        data['form'] = ProfesorForm(instance= profesor)

    else:
        data['form'] = ProfesorForm(request.POST, request.FILES, instance= profesor)  
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('listar_profesor') 

    template_name = 'profesor/agregar_profesor.html'
    return render(request, template_name, data)

def eliminarprofesor(request, profesor_id):
    data = {}
    profesor = Profesor.objects.get(pk=profesor_id)
    if request.method == "POST":
        profesor.delete()
        return redirect('listar_profesor')


    template_name = 'profesor/eliminar_profesor.html'
    return render(request, template_name, data)


#Alumno

def agregaralumno(request):
    data = {}
    if request.method == "POST":
        data['form'] = AlumnoForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('listar_alumno')

    else:
        data['form'] = AlumnoForm()
   

    template_name = 'alumno/agregar_alumno.html'
    return render(request, template_name, data)

def listaralumno(request):
    data = {}
    
    data['object_list'] = Alumno.objects.all().order_by('id')

    template_name = 'alumno/listar_alumno.html'
    return render(request, template_name, data)

def editaralumno(request, alumno_id):
    data = {}
    alumno = Alumno.objects.get(pk=alumno_id)
    if request.method == "GET":
        data['form'] = AlumnoForm(instance= alumno)

    else:
        data['form'] = AlumnorForm(request.POST, request.FILES, instance= alumno)  
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('listar_alumno') 

    template_name = 'alumno/agregar_alumno.html'
    return render(request, template_name, data)


def detallaralumno(request, alumno_id):
    data = {}
    data['alumno'] = Alumno.objects.get(pk=alumno_id)
    template_name = 'alumno/detallar_alumno.html'
    return render(request, template_name, data)

def eliminaralumno(request, alumno_id):
    data = {}
    alumno = Alumno.objects.get(pk=alumno_id)
    if request.method == "POST":
        alumno.delete()
        return redirect('listar_alumno')


    template_name = 'alumno/eliminar_alumno.html'
    return render(request, template_name, data)