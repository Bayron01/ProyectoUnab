from django.shortcuts import render
from django.shortcuts import redirect
from Universidad.models import Profesor, Alumno, Curso
from Universidad.forms import ProfesorForm, AlumnoForm, CursoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login')
def paginaprincipal(request):
	data = {}
	template_name = 'principal/pagina_principal.html'
	return render(request, template_name, data)


@login_required(login_url='/auth/login')
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

@login_required(login_url='/login_auth/login')
def listarprofesor(request):
    data = {}

    object_list = Profesor.objects.all().order_by('id')
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    
    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'profesor/listar_profesor.html'
    return render(request, template_name, data)

@login_required(login_url='/login_auth/login')
def detallarprofesor(request, profesor_id):
    data = {}
    data['profesor'] = Profesor.objects.get(pk=profesor_id)
    template_name = 'profesor/detallar_profesor.html'
    return render(request, template_name, data)

@login_required(login_url='/login_auth/login')
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

@login_required(login_url='/login_auth/login')
def eliminarprofesor(request, profesor_id):
    data = {}
    profesor = Profesor.objects.get(pk=profesor_id)
    if request.method == "POST":
        profesor.delete()
        return redirect('listar_profesor')


    template_name = 'profesor/eliminar_profesor.html'
    return render(request, template_name, data)


#Alumno

@login_required(login_url='/login_auth/login')
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

@login_required(login_url='/login_auth/login')
def listaralumno(request):
    data = {}

    object_list = Alumno.objects.all().order_by('id')
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    
    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'alumno/listar_alumno.html'
    return render(request, template_name, data)


@login_required(login_url='/login_auth/login')
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

@login_required(login_url='/login_auth/login')
def detallaralumno(request, alumno_id):
    data = {}
    data['alumno'] = Alumno.objects.get(pk=alumno_id)
    template_name = 'alumno/detallar_alumno.html'
    return render(request, template_name, data)


@login_required(login_url='/login_auth/login')
def eliminaralumno(request, alumno_id):
    data = {}
    alumno = Alumno.objects.get(pk=alumno_id)
    if request.method == "POST":
        alumno.delete()
        return redirect('listar_alumno')


    template_name = 'alumno/eliminar_alumno.html'
    return render(request, template_name, data)


#Curso


@login_required(login_url='/login_auth/login')
def agregarcurso(request):
    data = {}
    if request.method == "POST":
        data['form'] = CursoForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('listar_curso')

    else:
        data['form'] = CursoForm()
   

    template_name = 'curso/agregar_curso.html'
    return render(request, template_name, data)


@login_required(login_url='/login_auth/login')
def listarcurso(request):
    data = {}

    object_list = Curso.objects.all().order_by('id')
    paginator = Paginator(object_list, 5)
    page = request.GET.get('page')
    
    try:
        data['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data['object_list'] = paginator.page(1)
    except EmptyPage:
        data['object_list'] = paginator.page(paginator.num_pages)

    template_name = 'curso/listar_curso.html'
    return render(request, template_name, data)


@login_required(login_url='/login_auth/login')
def detallarcurso(request, curso_id):
    data = {}
    data['curso'] = Curso.objects.get(pk=curso_id)
    template_name = 'curso/detallar_curso.html'
    return render(request, template_name, data)


@login_required(login_url='/login_auth/login')
def editarcurso(request, curso_id):
    data = {}
    curso = Curso.objects.get(pk=curso_id)
    if request.method == "GET":
        data['form'] = CursoForm(instance= curso)

    else:
        data['form'] = CursoFormcurso(request.POST, request.FILES, instance= curso)  
        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()
            return redirect('listar_curso') 

    template_name = 'curso/agregar_curso.html'
    return render(request, template_name, data)


@login_required(login_url='/login_auth/login')
def eliminarcurso(request, curso_id):
    data = {}
    curso = Curso.objects.get(pk=curso_id)
    if request.method == "POST":
        curso.delete()
        return redirect('listar_curso')


    template_name = 'curso/eliminar_curso.html'
    return render(request, template_name, data)


