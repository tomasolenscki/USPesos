from django.shortcuts import render, get_list_or_404, redirect
from django.http import HttpResponse
from user.models import Professor
from .models import Treinos, Itemtreino, Aula
from .forms import AulaForm
from django.views.generic import UpdateView, CreateView

# Create your models here.

def home(request):
    context = {}
    return render(request, 'professores/home.html', context = context)

def solicita_treino(request):

    professor = Professor.objects.get(user=request.user)
    solicitacoes = Treinos.objects.filter(professor = professor).filter(criado = False).all()

    context = {
        'professor' : professor,
        'solicitacoes' : solicitacoes,
    }

    return render(request, 'professores/solicitacoes.html', context = context)


# def treino_add(request, pk):

#     treino = get_list_or_404(Treinos, aluno_id = pk).last()

#     if request.method == 'POST':
#         form = TreinoForm(request.POST)

#         if form.is_valid():


class AdicionaAula(CreateView):
    model = Aula
    form_class = AulaForm
    template_name = 'professores/nova_aula.html'
    success_url = '/professores/aulas'

    def form_valid(self, form):
        user = form.save()
        return redirect('professores:aulas')

def aulas(request):

    aulas = Aula.objects.all()
    professor = Professor.objects.get(user = request.user)

    context = {
        "aulas" : aulas,
        "professor" : professor,
    }

    return render(request, 'professores/aulas.html', context = context)
