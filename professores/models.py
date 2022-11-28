from django.db import models
from user.models import Aluno, Professor 

# Create your models here.

class Exercicio(models.Model):

    nome = models.CharField("Nome do exercício", blank=True, max_length= 255)
    urlfoto = models.CharField("URL da imagem do exercicio", blank=True, max_length= 255)
    maquina = models.CharField("Nome da máquina", blank=True, max_length= 255)


    def __str__(self):
        return self.nome + ' (' + self.maquina + ')'

class Treino(models.Model):

    # Itens próprios do treino
    nivel = models.IntegerField("Nível de dificuldade", blank=True)
    comentario = models.TextField("Comentários", blank = True)
    criado = models.BooleanField("Já foi montado?", blank= True, default = False)

    # Aluno e Professor envolvidos
    aluno = models.ForeignKey(Aluno, on_delete= models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete= models.CASCADE)

    def __str__(self):
        return 'treino de ' + self.aluno.user.name

class Itemtreino(models.Model):

    # Itens próprios do item treino
    carga = models.IntegerField("Carga do exercício", blank=True)
    repeticao = models.IntegerField("Número de repetições", blank=True)

    # Relação
    treino = models.ForeignKey(Treino, on_delete= models.CASCADE)
    exercicio = models.ForeignKey(Exercicio, on_delete= models.CASCADE)

    def __str__(self):
        return self.exercicio.nome

class Aula(models.Model):

    # Itens próprios
    dia = models.DateField("Dia da aula", blank = True)
    hora = models.TimeField("Horário da aula", blank = True)
    duracao = models.IntegerField("Duração da aula", blank = True, default=0)
    vagas = models.IntegerField("Número de vagas", blank = True , default=0)
    visivel = models.BooleanField("Visível", blank=True)
    modalidade = models.CharField("Modalidade da aula", blank = True, max_length= 255)
    inscritos = models.IntegerField("Número de inscritos", blank = True , default=0)

    # Relação
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.modalidade + ' do ' + self.professor.user.name

class Inscricao(models.Model):

    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    alunos = models.ManyToManyField(Aluno, blank = True)

    def __str__(self):
        return 'inscricao da aula ' + self.aula.modalidade




