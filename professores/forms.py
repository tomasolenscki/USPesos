from django import forms
from django.forms import ModelForm
from .models import Aula, Inscricao, Itemtreino
from django.db import transaction


class DateInput(forms.DateInput):
    input_type = 'date'

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = [
            'modalidade',
            'dia',
            'hora',
            'duracao',
            'vagas',
        ]
        widgets = {
            'dia': DateInput(),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'duracao': forms.TimeInput(attrs={'type': 'time'}),
        }


class ItemTreinoForm(ModelForm):
    class Meta:
        model = Itemtreino
        fields = ('carga', 'repeticao', 'exercicio', )