from django.shortcuts import render
from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from App1.models import Familia, Integrantes
from App1.forms import IntegrantesForm

# Create your views here.

def familiares(request):

    familiar1 = Familia.objects.get(pk=1)

    diccionario = {"familiar1": familiar1}

    familiar2 = Familia.objects.get(pk=2)

    diccionario["familiar2"] = familiar2

    familiar3 = Familia.objects.get(pk=3)

    diccionario["familiar3"] = familiar3

    plantilla = loader.get_template('plantilla1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def plantillaMVT(self):

    nombre = "Victor"
    apellido = "Frette"
    dia = datetime.now()
    notas = [5, 6, 3, 9, 2]

    diccionario = {"nombre":nombre, "apellido":apellido, "fecha":dia, "notas":notas}

    plantilla = loader.get_template('plantilla1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)  

def inicio(request):

    return render(request, 'App1/inicio.html') 

def plantillaUno(self):
    plantilla = loader.get_template('App1/padre.html')
    documento = plantilla.render

    return HttpResponse(documento)

def integrantes(request):

    familiar1 = Familia.objects.get(pk=1)

    diccionario = {"familiar1": familiar1}

    familiar2 = Familia.objects.get(pk=2)

    diccionario["familiar2"] = familiar2

    familiar3 = Familia.objects.get(pk=3)

    diccionario["familiar3"] = familiar3

    plantilla = loader.get_template('App1/integrantes.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def actividades(request):

    return render(request, 'App1/actividades.html')

def contacto(request):

    return render(request, 'App1/contacto.html')

def integrantesForm(request):

    if request.method == 'POST':

        miFormulario = IntegrantesForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            integrante = Integrantes(nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'],profesion=informacion['profesion'])

            integrante.save()

            return render(request, "App1/inicio.html")

    else:

        miFormulario = IntegrantesForm()

    return render(request, "App1/integrantesForm.html", {"miFormulario":miFormulario})

def buscarIntegrante(request):

    return render(request, "App1/buscarIntegrante.html")

def encontrarInt(request):

    if request.GET["apellido"]:
       
       #respuesta = f"Estoy buscando al integrante de apellido: {request.GET['apellido']}"
        apellido = request.GET['apellido']
        nombres = Integrantes.objects.filter(apellido__icontains=apellido)
    
        return render (request, "App1/resultadoBuscar.html", {"nombres":nombres, "apellido":apellido})

    else:

        respuesta = "No envió datos"

    return HttpResponse(respuesta)
