from django.shortcuts import render
from django.http import HttpResponse
from user.models import Aluno

# Create your models here.

def home(request):
    context = {}
    return render(request, 'alunos/home.html', context = context)

def perfil(request):

    if request.user.is_authenticated:
        aluno = Aluno.objects.get(user=request.user)
        context = {'aluno' : aluno}
        
    return render(request, 'alunos/perfil.html', context = context)