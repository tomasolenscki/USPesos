from django import forms
from .models import User, Aluno, Professor, Secretario
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model

class AlunoCadastroForm(UserCreationForm):

    # Padrão todos os usuários
    nome = forms.CharField(label='Nome*', required = True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Campos comuns com o professor
    cpf = forms.CharField(label='CPF*',required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email*', required = True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    nascimento = forms.DateField(label='Data de nascimento*', widget = forms.DateInput(format='%d/%m/%Y', attrs={'type':'date', 'class':'form-control'}), required = True)
    telefone = forms.CharField(label='Número de telefone*',required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    endereco = forms.CharField(label='Endereço',required = False, widget=forms.TextInput(attrs={'class':'form-control'}))
    urlfoto = forms.CharField(label='Url da Foto*',required = True, widget=forms.TextInput(attrs={'class':'form-control'}))

    # Campos exclusivos/perfil
    altura = forms.IntegerField(label='Altura (cm)',required = False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    peso = forms.IntegerField(label='Peso (kg)',required = False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    bracos = forms.IntegerField(label='Braços (cm)',required = False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    coxa = forms.IntegerField(label='Coxa (cm)',required = False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    peitoral = forms.IntegerField(label='Peitoral (cm)',required = False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    cinturaescapular = forms.IntegerField(label='Cintura escapular (cm)',required = False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    percentualgordura = forms.IntegerField(label='Percentual de gordura (%)',required = False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    secretario = forms.ModelChoiceField(label='Secretário responsável',queryset = Secretario.objects.all(), widget = forms.Select, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    @transaction.atomic
    def save(self):

        user = super().save(commit=False)
        user.is_aluno = True
        user.name = self.cleaned_data.get('nome')
        user.email = self.cleaned_data.get('email')

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
    nome = forms.CharField(label='Nome*', required = True, widget=forms.TextInput(attrs={'class':'form-control'}))

    # Campos comuns com o professor
    cpf = forms.CharField(label='CPF*', required = True, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email*', required = True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    # idade = forms.IntegerField(required = True)
    # telefone = forms.CharField(required = True)
    # endereco = forms.CharField(required = True)
    urlfoto = forms.CharField(label='URL da foto*',required = True, widget=forms.TextInput(attrs={'class':'form-control'}))

    # # Campos exclusivos
    cref = forms.CharField(label='CREF*',required = True, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    @transaction.atomic
    def save(self):

        user = super().save(commit=False)
        user.is_professor = True
        user.name = self.cleaned_data.get('nome')
        user.email = self.cleaned_data.get('email')

        user.save()

        professor = Professor.objects.create(user=user)
        professor.cpf = self.cleaned_data.get('cpf')
        professor.email = self.cleaned_data.get('email')
        # professor.idade.add(*self.cleaned_data.get('idade'))
        # professor.telefone.add(*self.cleaned_data.get('telefone'))
        # professor.endereco.add(*self.cleaned_data.get('endereco'))
        professor.urlfoto = self.cleaned_data.get('urlfoto')

        professor.cref = self.cleaned_data.get('cref')
        professor.save()

        return user



