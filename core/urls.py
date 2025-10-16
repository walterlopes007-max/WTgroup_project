from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)