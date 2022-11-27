from django import forms
from .models import User, Aluno, Professor, Secretario
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model

class AlunoCadastroForm(UserCreationForm):

    # Padrão todos os usuários
    nome = forms.CharField(required = True)

    # Campos comuns com o professor
    cpf = forms.CharField(label='CPF',required = True)
    email = forms.EmailField(required = False)
    nascimento = forms.DateField(label='Data de nascimento (mm/dd/aaaa)', required = True)
    telefone = forms.CharField(label='Número de telefone',required = False)
    endereco = forms.CharField(label='Endereço',required = False)
    urlfoto = forms.CharField(label='Url da Foto',required = False)

    # Campos exclusivos/perfil
    altura = forms.IntegerField(label='Altura (cm)',required = False)
    peso = forms.IntegerField(label='Peso (kg)',required = False)
    bracos = forms.IntegerField(label='Braços (cm)',required = False)
    coxa = forms.IntegerField(label='Coxa (cm)',required = False)
    peitoral = forms.IntegerField(label='Peitoral (cm)',required = False)
    cinturaescapular = forms.IntegerField(label='Cintura escapular (cm)',required = False)
    percentualgordura = forms.IntegerField(label='Percentual de gordura (%)',required = False)
    secretario = forms.ModelChoiceField(label='Secretário responsável',queryset = Secretario.objects.all(), widget = forms.Select, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    @transaction.atomic
    def save(self):

        user = super().save(commit=False)
        user.is_aluno = True
        user.name = self.cleaned_data.get('nome')

        user.save()

        aluno = Aluno.objects.create(user=user, secretario = self.cleaned_data.get('secretario'))

        aluno.cpf = self.cleaned_data.get('cpf')
        aluno.email = self.cleaned_data.get('email')
        aluno.nascimento = self.cleaned_data.get('nascimento')
        aluno.telefone = self.cleaned_data.get('telefone')
        aluno.endereco = self.cleaned_data.get('endereco')
        aluno.urlfoto = self.cleaned_data.get('urlfoto')

        aluno.altura = self.cleaned_data.get('altura')
        aluno.peso = self.cleaned_data.get('peso')
        aluno.bracos = self.cleaned_data.get('bracos')
        aluno.coxa= self.cleaned_data.get('coxa')
        aluno.peitoral= self.cleaned_data.get('peitoral')
        aluno.cinturaescapular= self.cleaned_data.get('cinturaescapular')
        aluno.percentualgordura = self.cleaned_data.get('percentualgordura')
        aluno.save()

        

        return user

class ProfessorCadastroForm(UserCreationForm):

    # Padrão todos os usuários
    nome = forms.CharField(required = True)

    # Campos comuns com o professor
    cpf = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    # idade = forms.IntegerField(required = True)
    # telefone = forms.CharField(required = True)
    # endereco = forms.CharField(required = True)
    # urlfoto = forms.CharField(required = True)

    # # Campos exclusivos
    # cref = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    @transaction.atomic
    def save(self):

        user = super().save(commit=False)
        user.is_professor = True
        user.name = self.cleaned_data.get('nome')

        user.save()

        professor = Professor.objects.create(user=user)
        professor.cpf = self.cleaned_data.get('cpf')
        professor.email = self.cleaned_data.get('email')
        # professor.idade.add(*self.cleaned_data.get('idade'))
        # professor.telefone.add(*self.cleaned_data.get('telefone'))
        # professor.endereco.add(*self.cleaned_data.get('endereco'))
        # professor.urlfoto.add(*self.cleaned_data.get('urlfoto'))

        # professor.cref.add(*self.cleaned_data.get('cref'))
        professor.save()

        return user



