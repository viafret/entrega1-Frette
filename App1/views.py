from django.shortcuts import render
from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader
from App1.models import Integrantes, Producto, Contacto
from App1.forms import IntegrantesForm, ProductoForm, ContactoForm

# Create your views here.

def inicio(request):

    return render(request, 'App1/inicio.html') 

def integrantes(request):
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

    return render(request, "App1/integrantes.html", {"miFormulario":miFormulario})


def producto(request):

    if request.method == 'POST':

        miFormulario = ProductoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            producto = Producto(nombre=informacion['nombre'], precio=informacion['precio'], stock=informacion['stock'])

            producto.save()

            return render(request, "App1/inicio.html")

    else:

        miFormulario = ProductoForm()

    return render(request, "App1/producto.html", {"miFormulario":miFormulario})
    

def contacto(request):

    if request.method == 'POST':

        miFormulario = ContactoForm(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            contacto = Contacto(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'])

            contacto.save()

            return render(request, "App1/inicio.html")

    else:

        miFormulario = ContactoForm()

    return render(request, "App1/contacto.html", {"miFormulario":miFormulario})
    

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

    