from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('universidades/', include('universidades.urls')),
    path('cursos/', include('cursos.urls')),
    path('carregar-cursos/', views.carregar_cursos),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre'),

]
