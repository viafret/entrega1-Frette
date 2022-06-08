from django import forms

class IntegrantesForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    profesion = forms.CharField()

class ProductoForm(forms.Form):

    nombre = forms.CharField (max_length=40)
    precio = forms.IntegerField()
    stock = forms.BooleanField()

class ContactoForm(forms.Form):

    nombre = forms.CharField (max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField ()
    telefono = forms.IntegerField ()