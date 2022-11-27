from django import forms
from django.forms import ModelForm
from professores.models import Treinos
from user.models import Aluno
from django.db import transaction

class TreinoForm(ModelForm):
    class Meta:
        model = Treinos
        fields = [
            'nivel',
            'comentario',
            'professor',
            'aluno',
        ]
        widgets = {
            'nivel': forms.Select(choices = ((1, 'fácil'), (2, 'médio'), (3, 'difícil')))
        }

class EditarPerfilForm(ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'email',
            'telefone',
            'endereco',
            'urlfoto',
            'altura',
            'peso',
            'bracos',
            'coxa',
            'peitoral',
            'cinturaescapular',
            'percentualgordura',

        ]

        labels = {
            'email':'Email',
            'telefone':'Telefone',
            'endereco':'Endereço',
            'urlfoto':'Url da foto',
            'altura':'Altura',
            'peso':'Peso',
            'bracos':'Braços',
            'coxa':'Coxa',
            'peitoral':'Peitoral',
            'cinturaescapular':'Cintura escapular',
            'percentualgordura':'Percentual de gordura',
        }
