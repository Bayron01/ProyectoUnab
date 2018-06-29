from django.urls import path
from Universidad import views


urlpatterns = [
    path('agregarprofesor', views.agregarprofesor, name='agregar_profesor'),

]