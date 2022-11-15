from django.shortcuts import render
from user.models import Aluno
from professores.models import Treinos
from django.views import generic
from alunos.forms import TreinoForm

# Create your models here.

def home(request):
    context = {}
    return render(request, 'alunos/home.html', context = context)

def perfil(request):

    if request.user.is_authenticated:
        aluno = Aluno.objects.get(user=request.user)
        context = {'aluno' : aluno}

    return render(request, 'alunos/perfil.html', context = context)

def meutreino(request):
    aluno = Aluno.objects.get(user=request.user)
    treino = Treinos.objects.filter(aluno = aluno).filter(Criado = True).last()
    itenstreino = treino.Itens_treino.all()
    context = {
        'treino' : treino,
        'itenstreino' : itenstreino}

    return render(request, 'alunos/meutreino.html', context = context)

class TreinoCreateView(generic.CreateView):
    model = Treinos
    form_class = TreinoForm
    template_name = 'alunos/novotreino.html'
    success_url = '/alunos/home/'


