from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'), # ruta pos defecto
    path('main', views.main, name='main'),
    path('login', views.inicio, name='inicio'), # viene del login de registro.html
    path('registro', views.registro, name='registro'), # viene del formulario de registro.html
    path('registrar', views.registrar, name='registrar'),
    path('logout', views.logout, name='logout'),
]