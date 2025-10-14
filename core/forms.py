from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)
