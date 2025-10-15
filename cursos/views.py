from django.shortcuts import render, get_object_or_404
from .models import Curso
from universidades.models import Universidade

def lista_cursos(request):
    universidade_id = request.GET.get('universidade')
    termo = request.GET.get('q')

    cursos = Curso.objects.select_related('universidade').order_by('universidade__nome', 'nome')
    universidades = Universidade.objects.all()

    if universidade_id:
        cursos = cursos.filter(universidade_id=universidade_id)
    if termo:
        cursos = cursos.filter(nome__icontains=termo)

    return render(request, 'cursos/lista.html', {
        'cursos': cursos,
        'universidades': universidades,
        'universidade_id': universidade_id,
        'termo': termo
    })

def curso_detalhe(request, curso_id):
    curso = get_object_or_404(Curso, id=curso_id)
    return render(request, 'cursos/detalhe.html', {'curso': curso})