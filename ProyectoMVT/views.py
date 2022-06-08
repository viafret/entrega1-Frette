from contextvars import Context
from datetime import datetime
from pipes import Template
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader


def plantillaMVT(self):

    nombre = "Victor"
    apellido = "Frette"
    dia = datetime.now()
    notas = [5, 6, 3, 9, 2]

    diccionario = {"nombre":nombre, "apellido":apellido, "fecha":dia, "notas":notas}

    #miHtml = open("C:/Users/victo/Documents/Python/Django/Proyecto1/ProyectoUno/ProyectoUno/plantillas/template1.html")

    #plantilla = Template(miHtml.read())

    #miHtml.close()

    plantilla = loader.get_template('plantilla2.html')

    
    #miContexto = Context(diccionario)

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)