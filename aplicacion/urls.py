from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('qwerty/', views.qwerty, name='qwerty'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('insertar/',views.insertar, name='insertar'),
    # path('', views.libros, name='libros'),
    # path('<int:libro_id>/', views.edit, name='edit'),
    # path('add_review/', views.add_review, name='add_review'),
]