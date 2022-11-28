from django.shortcuts import render, redirect
from user.models import Aluno, User
from professores.models import Treino, Aula, Itemtreino, Inscricao
from django.views import generic
from alunos.forms import TreinoForm, EditarPerfilForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your models here.

def home(request):
    context = {}
    return render(request, 'alunos/home.html', context = context)


def perfil(request):

    if request.user.is_authenticated:
        aluno = Aluno.objects.get(user=request.user)
        context = {'aluno' : aluno}

    return render(request, 'alunos/perfil.html', context = context)

# class PerfilUpdateView(generic.UpdateView):
#     form_class = EditarPerfilForm
#     model = Aluno
#     template_name = 'alunos/editarperfil.html'

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

def meutreino(request):
    aluno = Aluno.objects.get(user=request.user)
    treino = Treino.objects.filter(aluno = aluno).filter(criado = True).last()
    context={}
    if treino:
        itenstreino = Itemtreino.objects.filter( treino = treino).all()
        context = {
            'treino' : treino,
            'itenstreino' : itenstreino,
            }

    return render(request, 'alunos/meutreino.html', context = context)

class TreinoCreateView(generic.CreateView):
    model = Treino
    form_class = TreinoForm
    template_name = 'alunos/novotreino.html'
    success_url = '/alunos/home/'

def aulas(request):
    aulas = Aula.objects.filter(visivel = True).all()
    aluno = Aluno.objects.get(user = request.user)


    context = {
        "aulas" : aulas,
        "aluno" : aluno,
    }

    return render(request, 'alunos/aulas.html', context = context)

def inscricao(request, pk):

    aluno = Aluno.objects.get(user = request.user)
    aula = Aula.objects.get( pk = pk )
    inscricao = Inscricao.objects.get(aula = aula)

    if  int(inscricao.alunos.count()) < int(aula.vagas) and not Inscricao.objects.filter(aula = aula, alunos = aluno).all():

        inscricao.alunos.add(aluno)
        inscricao.save()
        aula.inscritos += 1
        aula.save()


    return redirect('alunos:aulas')




