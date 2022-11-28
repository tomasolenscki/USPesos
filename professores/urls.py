from django.urls import path
from . import views

# URLs dos usuários

app_name = 'professores'

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('solicitacoes/',views.solicita_treino, name = 'solicitacoes'),
    path('nova_aula/', views.AdicionaAula.as_view(), name = 'nova_aula'),
    path('aulas/', views.aulas, name = 'aulas'),
    path('solicitacoes/<int:pk>/',views.mostra_treino, name = 'mostra_treino'),
    path('solicitacoes/<int:pk>/add',views.treino_add_ex, name = 'add_ex_treino'),
    path('solicitacoes/<int:pk>/send',views.manda_treino, name = 'manda_treino'),
]