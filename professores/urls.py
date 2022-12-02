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
    path('solicitacoes/<int:pk>/delete/<int:pk2>/',views.treino_deleta_ex, name = 'deleta_ex_treino'),
    path('solicitacoes/<int:pk>/send',views.manda_treino, name = 'manda_treino'),
    path('aulas/<int:pk>/vis',views.visivel, name = 'aula_visivel'),
    path('aulas/<int:pk>/det',views.detalhe_aula, name = 'detalhe_aula'),
    path('aulas/<int:pk>/delete',views.DeletarAula.as_view(), name = 'deletar_aula'),
]