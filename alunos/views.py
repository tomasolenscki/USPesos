from django.shortcuts import render, redirect
from user.models import Aluno, User
from professores.models import Treino, Aula, Itemtreino, Inscricao
from .models import Sessao
from django.views import generic
from alunos.forms import TreinoForm, EditarPerfilForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from user.decorators import aluno_required
from django.utils.decorators import method_decorator
from datetime import datetime

# Create your models here.

@login_required
@aluno_required
def home(request):

    ultima_sessao = Sessao.objects.filter(aluno = Aluno.objects.get(user = request.user)).last()

    if request.user.is_authenticated:
        aluno = Aluno.objects.get(user=request.user)
        context = {'aluno' : aluno,
        'ultima_sessao' : ultima_sessao,
        }
    return render(request, 'alunos/home.html', context = context)

def iniciar_sessao(request):

    context = {}

    tempo_inicio = datetime.now()
    aluno = Aluno.objects.get(user = request.user)
    sessao = Sessao.objects.create(tempo_inicio = tempo_inicio, aluno = aluno)
    sessao.save()

    return redirect('alunos:home')      

def terminar_sessao(request):

    context = {}

    tempo_fim = datetime.now()
    aluno = Aluno.objects.get(user = request.user)
    sessao = Sessao.objects.filter(aluno = aluno).last()
    sessao.tempo_fim = tempo_fim
    sessao.save()

    return redirect('alunos:home')       


@login_required
@aluno_required
def perfil(request):

    if request.user.is_authenticated:
        aluno = Aluno.objects.get(user=request.user)
        context = {'aluno' : aluno}

    return render(request, 'alunos/perfil.html', context = context)

# class PerfilUpdateView(generic.UpdateView):
#     form_class = EditarPerfilForm
#     model = Aluno
#     template_name = 'alunos/editarperfil.html'

@login_required
@aluno_required
def editarperfil(request):
    if request.user.is_authenticated:
        aluno = Aluno.objects.get(user=request.user)
        # user = User.objects.get(user=request)

        if request.method == "POST":
            form = EditarPerfilForm(request.POST)

            if form.is_valid():
                # aluno.user.name = request.POST['name']
                aluno.email = form.cleaned_data['email']
                # aluno.nascimento = form.cleaned_data['nascimento']
                aluno.telefone = form.cleaned_data['telefone']
                aluno.endereco = form.cleaned_data['endereco']
                aluno.urlfoto = form.cleaned_data['urlfoto']
                aluno.altura = form.cleaned_data['altura']
                aluno.peso = form.cleaned_data['peso']
                aluno.bracos = form.cleaned_data['bracos']
                aluno.coxa = form.cleaned_data['coxa']
                aluno.peitoral = form.cleaned_data['peitoral']
                aluno.cinturaescapular = form.cleaned_data['cinturaescapular']
                aluno.percentualgordura = form.cleaned_data['percentualgordura']

                # aluno.user.save()
                aluno.save()
                return HttpResponseRedirect(reverse('alunos:perfil'))

        else:
            form = EditarPerfilForm(
            initial={
                'email': aluno.email,
                # 'nascimento': aluno.nascimento,
                'telefone': aluno.telefone,
                'endereco':aluno.endereco,
                'urlfoto':aluno.urlfoto,
                'altura':aluno.altura,
                'peso':aluno.peso,
                'bracos':aluno.bracos,
                'coxa':aluno.coxa,
                'peitoral':aluno.peitoral,
                'cinturaescapular':aluno.cinturaescapular,
                'percentualgordura':aluno.percentualgordura,
            })

        context = {'aluno' : aluno, 'form': form}
        return render(request, 'alunos/editarperfil.html', context = context)

@login_required
@aluno_required
def meutreino(request):
    aluno = Aluno.objects.get(user=request.user)
    treino = Treino.objects.filter(aluno = aluno).filter(criado = True).last()
    treino_vigente = Treino.objects.filter(aluno = aluno).filter(criado = False).last()
    context={}

    if treino and treino_vigente:
        itenstreino = Itemtreino.objects.filter( treino = treino).all()
        context = {
            'treino' : treino,
            'itenstreino' : itenstreino,
            'treino_vigente' : treino_vigente,
            }

    elif treino:
        itenstreino = Itemtreino.objects.filter( treino = treino).all()
        context = {
            'treino' : treino,
            'itenstreino' : itenstreino,
            }

    elif treino_vigente:
        context = {
            'treino' : treino,
            'treino_vigente' : treino_vigente,
            }

    return render(request, 'alunos/meutreino.html', context = context)

@method_decorator([login_required, aluno_required], name='dispatch')
class TreinoCreateView(generic.CreateView):
    model = Treino
    form_class = TreinoForm
    template_name = 'alunos/novotreino.html'
    success_url = '/alunos/meutreino/'

    def form_valid(self, form):
        treino = form.save(commit=False)
        treino.aluno = Aluno.objects.get(user = self.request.user)
        treino.save()
        return redirect('alunos:meutreino')

@login_required
@aluno_required
def aulas(request):
    aulas = Aula.objects.filter(visivel = True).all()
    aluno = Aluno.objects.get(user = request.user)


    context = {
        "aulas" : aulas,
        "aluno" : aluno,
    }

    return render(request, 'alunos/aulas.html', context = context)

@login_required
@aluno_required
def inscricao(request, pk):

    aluno = Aluno.objects.get(user = request.user)
    aula = Aula.objects.get( pk = pk )
    inscricao = Inscricao.objects.get(aula = aula)

    if  int(inscricao.alunos.count()) < int(aula.vagas) and not Inscricao.objects.filter(aula = aula, alunos = aluno).all():

        inscricao.alunos.add(aluno)
        inscricao.save()
        aula.inscritos += 1
        aula.save()

        messages.success(request, 'Você se inscreveu na aula com sucesso!')
    
    else:

        messages.warning(request, 'Você já está inscrito ou a turma está cheia!')

    return redirect('alunos:aulas')

@login_required
@aluno_required
def desinscricao(request, pk):
    
    aluno = Aluno.objects.get(user = request.user)
    aula = Aula.objects.get( pk = pk )
    inscricao = Inscricao.objects.get(aula = aula)

    if Inscricao.objects.filter(aula = aula, alunos = aluno).all():
        inscricao.alunos.remove(aluno)
        inscricao.save()
        aula.inscritos -= 1
        aula.save()

    return redirect('alunos:aulas')



