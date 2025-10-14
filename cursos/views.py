from django.shortcuts import render, get_object_or_404
from .models import Curso

def lista_cursos(request):
    cursos = Curso.objects.all().select_related('universidade')
    return render(request, 'cursos/lista.html', {'cursos': cursos})

def curso_detalhe(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/detalhe.html', {'curso': curso})
