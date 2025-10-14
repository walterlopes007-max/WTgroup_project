from django import forms
from .models import Universidade

class UniversidadeForm(forms.ModelForm):
    class Meta:
        model = Universidade
        fields = ['nome', 'descricao', 'imagem']
