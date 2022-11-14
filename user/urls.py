from django.urls import path
from . import views

# URLs dos usuários

app_name = 'user'

urlpatterns = [
    path('cadastro/',views.register, name='cadastro'),
    path('cadastro_aluno/',views.Aluno_register.as_view(), name='cadastro_aluno'),
    path('cadastro_professor/',views.Professor_register.as_view(), name='cadastro_professor'),
]