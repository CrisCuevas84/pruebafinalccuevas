from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'), # ruta pos defecto
    path('login', views.inicio, name='inicio'), # viene del login de registro.html
    path('registro', views.registro, name='registro'), # viene del formulario de registro.html
    path('login2', views.login2, name='login2'), # otro acceso al login desde navbar del registro
    path('registrar', views.registrar, name='registrar'),
    path('logout', views.logout, name='logout'),
    path('users/<int:user_id>', views.view_user, name='view_user'),
    path('cambiar_pass', views.cambiar_pass, name='cambiar_pass'),
]