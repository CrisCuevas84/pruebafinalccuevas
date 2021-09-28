from django.shortcuts import render, redirect
from django.contrib import messages
from acceso.models import *
# Create your views here.


def index(request):
    if 'user_id' not in request.session:
        return redirect('login')
    
    context = {
        "active_user": User.objects.get(id=request.session['user_id']),
        'viajes': Viaje.objects.all(),
    }
    return render(request, 'aplicacion.html', context)


def add(request):
    hello = "Hola"
    context ={
        'saludo': hello,
        'travels': Viaje.objects.all(),
    }
    return render(request, 'aplicacion_2.html', context)


def destination(request):    
    context ={
        'viajes': Viaje.objects.all(),
    }
    return render(request, 'destination.html', context)


def recuperar(request):
    reg_user = User.objects.get(id=request.session['user_id'])

    context = {
        "active_user": reg_user,
    }
    return render(request, 'rec_pass.html', context)


def insertar(request):
    # Rescatando la info desde el Review
    # con variables errores, vamos a capturar errores
    errores = {}

    if len(request.POST['destino']) == 0:
        errores['review'] = "Debe ingresar un destino"

    if len(request.POST['descripcion']) == 0:
        errores['rating'] = "Debe agregar una descripcion"

    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return render(request, 'agregar.html')
    else:    
        viaje = Viaje.objects.create(
            destino=request.POST['destino'], 
            descripcion=request.POST['descripcion'],
            travel_start=request.POST['datestart'],
            travel_end=request.POST['dateend'],
        )
        viaje.usuarios.add(User.objects.get(id=request.session['user_id']))
        return redirect('/')

