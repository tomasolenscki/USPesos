from django import forms
from django.forms import ModelForm
from professores.models import Treino
from user.models import Aluno
from django.db import transaction

# class FormataComentario(forms.TextInput):
#     class = 'form-control'

class TreinoForm(ModelForm):
    class Meta:
        model = Treino
        fields = [
            'nivel',
            'comentario',
            'professor',
        ]
        widgets = {
            'nivel': forms.Select(choices = ((1, 'fácil'), (2, 'médio'), (3, 'difícil'))),
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

        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'telefone': forms.TextInput(attrs={'class':'form-control'}),
            'endereco': forms.TextInput(attrs={'class':'form-control'}),
            'urlfoto': forms.TextInput(attrs={'class':'form-control'}),
            'altura': forms.NumberInput(attrs={'class':'form-control'}),
            'peso': forms.NumberInput(attrs={'class':'form-control'}),
            'bracos': forms.NumberInput(attrs={'class':'form-control'}),
            'coxa': forms.NumberInput(attrs={'class':'form-control'}),
            'peitoral': forms.NumberInput(attrs={'class':'form-control'}),
            'cinturaescapular': forms.NumberInput(attrs={'class':'form-control'}),
            'percentualgordura': forms.NumberInput(attrs={'class':'form-control'}),
        }
