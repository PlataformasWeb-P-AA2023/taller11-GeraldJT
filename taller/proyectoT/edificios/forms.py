from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from edificios.models import *

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del edificio'),
            'direccion': _('Ingrese la direccion'),
            'ciudad': _('Ingrese la ciudad de locacion'),
            'tipo': _('Seleccione el tipo de edificio'),
        }


    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']

        if valor[0:1] == "L":
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con L")
        return valor

class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_Propietario', 'costo', 'numero_cuartos', 'edificio']
        labels = {
            'nombre_Propietario': _('Ingrese los nombres completos del propietario'),
            'costo': _('Ingrese el costo del departamento'),
            'numero_cuartos': _('Ingrese el numero de cuartos'),
            'edificio': _('Ingrese el deficio al que pertenece'),
        }


    def clean_costo(self):
        valor = self.cleaned_data['costo']

        if valor > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a 100 mil")
        return valor
    
    def clean_numero_cuartos(self):
        valor = self.cleaned_data['costo']

        if valor > 100000:
            raise forms.ValidationError("El costo no puede ser mayor a 100 mil")
        return valor






