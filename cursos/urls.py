from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.lista_cursos, name='lista_cursos'),
    path('<int:id>/', views.detalhe_curso, name='detalhe_curso'),  
]

