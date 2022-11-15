from django.db import models
from user.models import Aluno, Professor 

# Create your models here.

class Exercicio(models.Model):

    nome = models.CharField("Nome do exercício", blank=True, max_length= 255)
    urlfoto = models.CharField("URL da imagem do exercicio", blank=True, max_length= 255)

class Itemtreino(models.Model):

    # Itens próprios do item treino
    carga = models.IntegerField("Carga do exercício", blank=True)

    # Relação
    exercicios = models.ManyToManyField(Exercicio, blank=True)

class Treinos(models.Model):

    # Itens próprios do treino
    nivel = models.IntegerField("Nível de dificuldade", blank=True)
    comentario = models.TextField("Comentários", blank = True)
    Criado = models.BooleanField("Já foi montado?", blank= True, default = False)

    # Aluno e Professor envolvidos
    aluno = models.ForeignKey(Aluno, on_delete= models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete= models.CASCADE)

    # Itens que compõem o treino
    Itens_treino = models.ManyToManyField(Itemtreino, blank=True)

class Aula(models.Model):

    # Itens próprios
    data = models.DateTimeField("Dia e hora da aula", blank = True)
    visível = models.BooleanField("Visível", blank=True)

    # Relação
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

class Inscricao(models.Model):

    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno, blank = True)




