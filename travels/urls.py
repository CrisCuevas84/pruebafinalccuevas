from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('destination/', views.destination, name='destination'),
    path('add/', views.add, name='add'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('insertar/',views.insertar, name='insertar'),
]
