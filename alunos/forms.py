from django import forms
from django.forms import ModelForm
from professores.models import Treinos
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

