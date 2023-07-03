from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from ordenamiento.models import *

# importar los formularios de forms.py
from ordenamiento.forms import *

# Create your views here.

def index(request):
    
    return render(request, 'index.html')


def mostrar_Parroquias_Barrios(request):
    
    parroquia = Parroquia.objects.all()
    barrio = Barrio.objects.all()
    informacion_template = {'parroquia': parroquia, 'numero_parroquia':len(parroquia), 'barrio': barrio}
    return render(request, 'parroquia_barrio.html', informacion_template)


def obtener_Barrios(request, id):
    
    parroquia = Parroquia.objects.get(pk=id)
    barrio = Barrio.objects.filter(parroquia = id)
    informacion_template = {'barrio': barrio, 'parroquia': parroquia}
    return render(request, 'obtenerBarrios.html', informacion_template)

def mostrar_Barrios(request):
    
    
    barrio = Barrio.objects.all()
    informacion_template = {'barrio': barrio}
    return render(request, 'mostrarBarrios.html', informacion_template)


def crear_parroquia(request):
    """
    """
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)


def editar_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)


def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)

def crear_barrio_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia }

    return render(request, 'crearBarrioParroquia.html', diccionario)
