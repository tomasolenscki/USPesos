from django.db import models
from user.models import Aluno

class Sessao(models.Model):

    tempo_inicio = models.TimeField("Início da sessão", blank = True)
    tempo_fim = models.TimeField("Fim da sessão", null = True)
    aluno = models.ForeignKey(Aluno, on_delete= models.CASCADE)



