from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse #importamos para que la repuesta llegue a django

def inicio1(request): #definimos la funcion del inicio
    return HttpResponse("este es el inicio de nuestra aplicacion de los alumnos")
#indica lo que queremos mostrar en la vista 


