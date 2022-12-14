from django import forms
from django.forms import ModelForm
from .models import Aula, Inscricao, Itemtreino
from django.db import transaction

class AulaForm(ModelForm):
    class Meta:
        model = Aula
        fields = [
            'modalidade',
            'professor',
            'dia',
            'hora',
            'duracao',
            'vagas',
        ]
        widgets = {
            'dia': forms.DateTimeInput(attrs={'class': 'datepicker'}),
            'modalidade' : forms.Select(choices= (('Ioga','Ioga'), ('Spinning','Spinning'), ('Pilates','Pilates'),('Zuumba','Zuumba')))
        }
    
    @transaction.atomic
    def save(self):

        aula = super().save(commit=False)
        aula.visivel = False

        aula.save()

        inscricao = Inscricao.objects.create(aula = aula)

        inscricao.save()


        return aula

class ItemTreinoForm(ModelForm):
    class Meta:
        model = Itemtreino
        fields = ('carga', 'repeticao', 'exercicio', )