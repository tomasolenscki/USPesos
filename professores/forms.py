from django import forms
from django.forms import ModelForm
from .models import Aula, Inscricao
from django.db import transaction

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = [
            'modalidade',
            'dia',
            'hora',
            'duracao',
            'vagas',
            'professor',
        ]
        widgets = {
            'dia': forms.DateTimeInput(attrs={'class': 'datepicker'}),
        }
    
    @transaction.atomic
    def save(self):

        aula = super().save(commit=False)
        aula.visivel = False

        aula.save()

        inscricao = Inscricao.objects.create(aula = aula)

        inscricao.save()


        return aula