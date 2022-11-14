from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import AlunoCadastroForm, ProfessorCadastroForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth import login, logout,authenticate
from django.contrib import messages

# Create your views here.

# View de escolha entre registrar como aluno ou professor
def register(request):
    return render(request, 'user/cadastro.html')

# View para o cadastro de aluno
class Aluno_register(CreateView):
    model = User
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
    model = User
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

# View de login
# def login_request(request):
#     if request.method=='POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None :
#                 login(request,user)
#                 return redirect('/')
#             else:
#                 messages.error(request,"Invalid username or password")
#         else:
#                 messages.error(request,"Invalid username or password")
#     return render(request, 'user/login.html',
#     context={'form':AuthenticationForm()})

# View de logout
# def logout_view(request):
#     logout(request)
#     return redirect('/')