from django.db import models

class Universidade(models.Model):
    nome = models.CharField(max_length=200)
    pais = models.CharField(max_length=100)
    descricao = models.TextField()
    site = models.URLField(blank=True, null=True)
    imagem = models.ImageField(upload_to='universidades/', blank=True, null=True)

    def __str__(self):
        return self.nome
