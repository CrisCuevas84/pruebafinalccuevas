from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from time import gmtime, strftime
from django.db.models import Count
import bcrypt

from .models import *

# Create your views here.

def login(request):
    return redirect('main')


def main(request):
    if 'user_id' in request.session:
        return redirect('travels/')
    return render(request, 'registro.html')


def inicio(request):
    usuario = User.objects.filter(username=request.POST['username2'].lower())
    errores = User.objects.validar_login(request.POST['password'], usuario)

    if len(errores) > 0:
        for key, msg in errores.items():
            messages.error(request, msg)
        return redirect('/')
    else:
        request.session['user_id'] = usuario[0].id
        request.session['user_name'] = usuario[0].nombre
        return redirect('travels/')


def registrar(request):
    return render(request, 'registro.html')        


def registro(request):
    #validacion de parametros
    errors = User.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, msg in errors.items():
            messages.error(request, msg)
        return redirect('/registrar')

    else:
        #encriptar password
        password = User.objects.encriptar(request.POST['password'])
        
        rol = 2
        if User.objects.all().count() == 0:
            rol = 1

        #crear usuario
        user = User.objects.create(
            nombre=request.POST['nombre'],
            username=request.POST['username'],
            password=password,
        )
        #request.session['user_id'] = user.id
        #retornar mensaje de creacion correcta
        msg="Usuario creado exitosamente!"
        messages.success(request, msg)
    return redirect('/')


def logout(request):
    request.session.flush()
    return redirect('/')


