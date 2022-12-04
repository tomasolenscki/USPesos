from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user.decorators import admin_required
from django.utils.decorators import method_decorator
from professores.models import Professor, Aluno, Treino, Aula, Modalidade
from user.models import Secretario
from alunos.models import Sessao
import datetime
from datetime import date

# Create your views here.
@login_required
@admin_required
def home(request):
    context = {}
    return render(request, 'secretaria/home.html', context = context)

@login_required
@admin_required
def dados(request):
    alunos = Aluno.objects.all()

    idades = 0
    for aluno in alunos:
        idade = date.today().year - aluno.nascimento.year
        idades += idade

    if len(alunos) != 0:
        media_idades = round(idades/len(alunos), 2)
    else:
        media_idades = 0

    professores = Professor.objects.all()

    treinos = []
    for professor in professores:
        treino = Treino.objects.filter(professor = professor).all()
        treinos.append((professor.user.name, treino.count()))

    aulas_por_modalidade = []
    modalidades = Modalidade.objects.all()
    for modalidade in modalidades:
        aulas = Aula.objects.filter(modalidade = modalidade).all()
        numero_de_aulas = aulas.count()
        aulas_por_modalidade.append((modalidade.nome, numero_de_aulas))

    professor_do_mes = professores.last()
    a = 0

    aulas_por_professor = []
    for professor in professores:
        aulas = Aula.objects.filter(professor = professor).all()
        numero_de_aulas = aulas.count()
        if numero_de_aulas > a:
            professor_do_mes = professor
            a = numero_de_aulas

        aulas_por_professor.append((professor.user.name, numero_de_aulas))

    secretarios = Secretario.objects.all()
    total_secretarios = secretarios.count()

    ultimo_aluno_cadastrado = alunos.last()

    ultimo_professor_cadastrado = professores.last()


    alunos_por_secretarios = []
    for secretario in secretarios:
        alunos_cadastrados = alunos.filter(secretario = secretario)
        alunos_por_secretarios.append((secretario.name, alunos_cadastrados.count()))

    sessoes = Sessao.objects.all()
    tempo_sessao = 0
    numero_sessoes = 0
    if sessoes and sessoes.first().tempo_fim:
        for sessao in sessoes:
            if sessao.tempo_fim:
                tempo_sessao += (sessao.tempo_fim.hour - sessao.tempo_inicio.hour)*60 + sessao.tempo_fim.minute - sessao.tempo_inicio.minute
                numero_sessoes += 1
        media_de_tempos = round(tempo_sessao/numero_sessoes, 2)

    else:
        media_de_tempos = 0

    


    context = {
        'alunos' : alunos,
        'media_idades' : media_idades,
        'professores' : professores,
        'treinos' : treinos,
        'aulas' : aulas_por_modalidade,
        'aulas_prof' : aulas_por_professor,
        'secretarios' : total_secretarios,
        'ultimo_aluno' : ultimo_aluno_cadastrado,
        'ultimo_professor' : ultimo_professor_cadastrado,
        'alunos_por_secretarios' : alunos_por_secretarios,
        'media_tempos' : media_de_tempos,
        'professor_do_mes' : professor_do_mes,
        }
    return render(request, 'secretaria/dados.html', context = context)