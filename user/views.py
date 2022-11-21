from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
from .forms import AlunoCadastroForm, ProfessorCadastroForm
from .models import User
from django.contrib.auth import login
from django.contrib.auth import get_user_model

# Create your views here.

# View de escolha entre registrar como aluno ou professor
def register(request):
    return render(request, 'user/cadastro.html')

# View para o cadastro de aluno
class Aluno_register(CreateView):
    model = get_user_model()
    form_class = AlunoCadastroForm
    template_name = 'user/cadastro_aluno.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'aluno'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user:cadastro')

# View para o cadastro de professor
class Professor_register(CreateView):
    model = get_user_model()
    form_class = ProfessorCadastroForm
    template_name = 'user/cadastro_professor.html'
    success_url = '/user/register/'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('user:cadastro')

def home(request):
    if request.user.is_authenticated:
        if request.user.is_professor:
            return redirect('professores:home')
        elif request.user.is_aluno: 
            return redirect('alunos:home')
        else:
            return redirect('secretaria:home')

    else:
        return redirect('user:cadastro')

def login2(request):
    return HttpResponseRedirect(reverse('login'))
