from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from datetime import datetime, date

# Create your models here.

class Secretario(models.Model):
    name = models.CharField(_("Nome do secretario"), blank=True, max_length=255)

    def __str__(self):
        return self.name

class User(AbstractUser):

    is_aluno = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)

    name = models.CharField(_("Nome do usuário"), blank=True, max_length=255)


class Aluno(models.Model):

    # Link com o User
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)

    # Campos comuns com o professor
    cpf = models.CharField("CPF", blank=True, max_length=14)
    email = models.EmailField("E-mail", blank=True)
    nascimento = models.DateField(_("Data de Nascimento"), auto_now_add=False, auto_now=False, blank=True, null=True)
    telefone = models.CharField(_("Número de telefone"), blank=True, max_length=20)
    endereco = models.CharField(_("Endereço"), blank=True, max_length=255)
    urlfoto = models.CharField(_("URL da foto"), blank=True, max_length=255)

    # Campos exclusivos/perfil
    altura = models.IntegerField(_("Altura"), blank=True, null=True)
    peso = models.IntegerField(_("Peso"), blank=True, null=True)
    bracos = models.IntegerField(_("Braços"), blank=True, null=True)
    coxa = models.IntegerField(_("Coxa"), blank=True, null=True)
    peitoral = models.IntegerField(_("Peitoral"), blank=True, null=True)
    cinturaescapular = models.IntegerField(_("Cintura Escapular"), blank=True, null=True)
    percentualgordura = models.IntegerField(_("Percentual de Gordura"), blank=True, null=True)

    secretario = models.ForeignKey(Secretario, on_delete= models.CASCADE, related_name='aluno')

    def __str__(self):
        return self.user.name




class Professor(models.Model):

    # Link com o User
    user = models.OneToOneField(User, on_delete= models.CASCADE, primary_key= True)

    # Campos comuns com o aluno
    cpf = models.CharField("CPF", blank=True, max_length=14)
    email = models.EmailField("E-mail", blank=True)
    # idade = models.IntegerField(_("Idade"), blank=True)
    # telefone = models.CharField(_("Número de telefone"), blank=True, max_length=20)
    # endereco = models.CharField(_("Endereço"), blank=True, max_length=255)
    # urlfoto = models.CharField(_("URL da foto"), blank=True, max_length=255)

    # #Campos exclusivos
    cref = models.CharField("CREF", blank=True, max_length=14)

    def __str__(self):
        return self.user.name











