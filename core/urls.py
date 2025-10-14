from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from . import views  

def home(request):
    return HttpResponse("<h1>Bem-vindo ao sistema WTgroup</h1><p>Use /universidades/ para listar as universidades.</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('universidades/', include('universidades.urls')),
    path('', views.home, name='home'),
    path('cursos/', include('cursos.urls')),
    path('contato/', views.contato, name='contato'),
    path('contato/', include('core.contato_urls')),
    path('sobre/', views.sobre, name='sobre'),
]
