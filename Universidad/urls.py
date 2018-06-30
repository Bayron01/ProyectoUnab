from django.urls import path
from Universidad import views


urlpatterns = [
	
	path('paginaprincipal', views.paginaprincipal, name='pagina_principal'),

	#Profesor
    path('agregarprofesor', views.agregarprofesor, name='agregar_profesor'),
    path('listarprofesor', views.listarprofesor, name='listar_profesor'),
    path('detallarprofesor/<int:profesor_id>', views.detallarprofesor, name='detallar_profesor'),
    path('editarprofesor/<int:profesor_id>', views.editarprofesor, name='editar_profesor'),
    path('eliminarprofesor/<int:profesor_id>', views.eliminarprofesor, name="eliminar_profesor"),

    #Alumno
    path('agregaralumno', views.agregaralumno, name='agregar_alumno'),
    path('listaralumno', views.listaralumno, name='listar_alumno'),

]