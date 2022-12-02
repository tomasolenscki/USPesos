from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.http import HttpResponse
from user.models import Professor
from .models import Treino, Itemtreino, Aula, Inscricao, Exercicio
from .forms import AulaForm, ItemTreinoForm
from django.views.generic import UpdateView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from user.decorators import professor_required
from django.utils.decorators import method_decorator

# Create your models here.

@login_required
@professor_required
def home(request):
    context = {}
    return render(request, 'professores/home.html', context = context)

@login_required
@professor_required
def solicita_treino(request):

    professor = Professor.objects.get(user=request.user)
    solicitacoes = Treino.objects.filter(professor = professor).filter(criado = False).all()

    context = {
        'professor' : professor,
        'solicitacoes' : solicitacoes,
    }

    return render(request, 'professores/solicitacoes.html', context = context)

@login_required
@professor_required
def mostra_treino(request, pk):

    treino = get_object_or_404(Treino, pk = pk, professor = Professor.objects.get(user = request.user))
    itenstreino = Itemtreino.objects.filter(treino = treino).all()

    context = {
        'itenstreino' : itenstreino,
        'pk' : pk
    }

    return render(request, 'professores/solicitacao.html', context= context)

@login_required
@professor_required
def manda_treino(request, pk):

    treino = get_object_or_404(Treino, pk = pk, professor = Professor.objects.get(user = request.user))
    treino.criado = True
    treino.save()

    return redirect('professores:solicitacoes')

@login_required
@professor_required
def treino_add_ex(request, pk):

    treino = get_object_or_404(Treino, pk = pk, professor = Professor.objects.get(user = request.user))


    if request.method == 'POST':

        form = ItemTreinoForm(request.POST)

        if form.is_valid():
            itens_treino = form.save(commit=False)
            itens_treino.treino = treino
            itens_treino.save()

        return redirect('professores:mostra_treino', pk)

    else:

        form = ItemTreinoForm()

    return render(request, 'professores/montar.html', { 'treino' : treino, 'form' : form })

@method_decorator([login_required, professor_required], name='dispatch')
class AdicionaAula(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'professores/nova_aula.html'
    success_url = '/professores/aulas'

@login_required
@professor_required
def aulas(request):

    aulas = Aula.objects.all()
    professor = Professor.objects.get(user = request.user)

    context = {
        "aulas" : aulas,
        "professor" : professor,
    }

    return render(request, 'professores/aulas.html', context = context)

@login_required
@professor_required
def visivel(request, pk):
    aula = get_object_or_404(Aula, pk = pk, professor = Professor.objects.get(user = request.user))

    if aula.visivel:
        aula.visivel = False
    else:
        aula.visivel = True
    
    aula.save()

    return redirect('professores:aulas')

@login_required
@professor_required
def detalhe_aula(request, pk):

    aula = get_object_or_404(Aula, pk = pk)

    alunos = Inscricao.objects.get(aula = aula).alunos.all()

    context = {
        'aula' : aula,
        'alunos' : alunos,
    }

    return render(request, 'professores/detalhe_aula.html', context= context)

@method_decorator([login_required, professor_required], name='dispatch')
class DeletarAula(DeleteView):
    model = Aula
    success_url = '/professores/aulas'
    template_name = 'professores/deletaraula.html'
