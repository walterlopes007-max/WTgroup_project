from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContatoForm

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/lista.html', {'cursos': cursos})

def contato(request):
    sucesso = False  # variável de controle

    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            # Conteúdo do e-mail
            assunto = f"Mensagem de contato de {nome}"
            corpo = f"Nome: {nome}\nE-mail: {email}\n\nMensagem:\n{mensagem}"

            # Envia o e-mail
            send_mail(
                assunto,
                corpo,
                settings.DEFAULT_FROM_EMAIL,  # remetente
                [settings.CONTACT_EMAIL],      # destinatário
                fail_silently=False,
            )

            sucesso = True
    else:
        form = ContatoForm()

    return render(request, 'contato.html', {'form': form, 'sucesso': sucesso})

def sobre(request):
    return render(request, 'sobre.html')

def home(request):
    return render(request, 'home.html')
from django.core.management import call_command
from django.http import HttpResponse

def carregar_cursos(request):
    call_command('loaddata', 'cursos_backup_fixed.json')
    return HttpResponse("✅ Cursos carregados com sucesso no Render!")
