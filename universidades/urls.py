from django.urls import path
from . import views

urlpatterns = [
    # Rota principal — mostra a lista de universidades
    path('', views.lista, name='lista_universidades'),

    # Rota de detalhes — mostra detalhes de uma universidade específica
    path('<int:universidade_id>/', views.detalhe_universidade, name='detalhe_universidade'),
]
