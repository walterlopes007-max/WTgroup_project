from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='cursos'),
    path('<int:curso_id>/', views.curso_detalhe, name='curso_detalhe'),
]

