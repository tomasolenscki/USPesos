from django import forms
from .models import User, Aluno, Professor, Secretario
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.contrib.auth import get_user_model

class AlunoCadastroForm(UserCreationForm):

    # Padrão todos os usuários
    nome = forms.CharField(required = True)

    # Campos comuns com o professor
    cpf = forms.CharField(required = True)
    email = forms.EmailField(required = False)
    # idade = forms.IntegerField(required = False)
    # telefone = forms.CharField(required = False)
    # Endereco = forms.CharField(required = False)
    # urlfoto = forms.CharField(required = False)

    # # Campos exclusivos/perfil
    # altura = forms.IntegerField(required = False)
    # peso = forms.IntegerField(required = False)
    # bracos = forms.IntegerField(required = False)
    # coxa = forms.IntegerField(required = False)
    # peitoral = forms.IntegerField(required = False)
    # cinturaescapular = forms.IntegerField(required = False)
    # percentualgordura = forms.IntegerField(required = False)
    secretario = forms.ModelChoiceField(queryset = Secretario.objects.all(), widget = forms.Select, required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()

    @transaction.atomic
    def save(self):

        user = super().save(commit=False)
        user.is_aluno = True
        user.name = self.cleaned_data.get('nome')

        user.save()

        aluno = Aluno.objects.create(user=user)
        aluno.cpf = self.cleaned_data.get('cpf')
        aluno.email = self.cleaned_data.get('email')
        aluno.secretario.add(*self.cleaned_data.get('secretario'))
        # aluno.idade.add(*self.cleaned_data.get('idade'))
        # aluno.telefone.add(*self.cleaned_data.get('telefone'))
        # aluno.Endereco.add(*self.cleaned_data.get('Endereco'))
        # aluno.urlfoto.add(*self.cleaned_data.get('urlfoto'))

        # aluno.altura.add(*self.cleaned_data.get('altura'))
        # aluno.peso.add(*self.cleaned_data.get('peso'))
        # aluno.bracos.add(*self.cleaned_data.get('bracos'))
        # aluno.coxa.add(*self.cleaned_data.get('coxa'))
        # aluno.peitoral.add(*self.cleaned_data.get('peitoral'))
        # aluno.cinturaescapular.add(*self.cleaned_data.get('cinturaescapular'))
        # aluno.percentualgordura.add(*self.cleaned_data.get('percentualgordura'))
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
    # Endereco = forms.CharField(required = True)
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
        # professor.Endereco.add(*self.cleaned_data.get('Endereco'))
        # professor.urlfoto.add(*self.cleaned_data.get('urlfoto'))

        # professor.cref.add(*self.cleaned_data.get('cref'))
        professor.save()

        return user



