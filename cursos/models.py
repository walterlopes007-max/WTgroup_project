from django.db import models
from universidades.models import Universidade

class Curso(models.Model):
    GRAU_OPCOES = [
        ('Bachelor', 'Licenciatura / Bachelor'),
        ('Master', 'Mestrado / Master'),
        ('PhD', 'Doutoramento / PhD'),
    ]

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    duracao = models.CharField(max_length=50)
    grau = models.CharField(max_length=20, choices=GRAU_OPCOES)
    universidade = models.ForeignKey(Universidade, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='cursos/', blank=True, null=True),

    def __str__(self):
        return f"{self.nome} ({self.universidade.nome})"

