from django.urls import path
from Universidad import views


urlpatterns = [
	
	path('paginaprincipal', views.paginaprincipal, name='pagina_principal'),
    path('agregarprofesor', views.agregarprofesor, name='agregar_profesor'),

]