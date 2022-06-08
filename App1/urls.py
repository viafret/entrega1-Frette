from django import views
from django.urls import path
from App1 import views

urlpatterns = [
    
    path('', views.inicio, name="Inicio"),
    path('integrantes/', views.integrantes, name="Integrantes"),
    #path('actividades/', views.actividades, name="Actividades"),
    path('producto/', views.producto, name="Producto"),
    path('contacto/', views.contacto, name="Contacto"),
    #path('integrantesForm/', views.integrantesForm, name="integrantesForm"),
    path('buscarIntegrante/', views.buscarIntegrante, name="buscarIntegrante"),
    path('buscar/', views.encontrarInt),
]