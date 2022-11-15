from django.urls import path
from . import views

# URLs dos usuários

app_name = 'alunos'

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('perfil/',views.perfil, name = 'perfil'),
]