from django import forms

class IntegrantesForm(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    edad = forms.IntegerField()
    profesion = forms.CharField()
