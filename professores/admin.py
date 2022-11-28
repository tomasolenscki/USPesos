from django.contrib import admin
from .models import Exercicio, Itemtreino, Aula, Inscricao, Treino

# Register your models here.

admin.site.register(Exercicio)
admin.site.register(Itemtreino)
admin.site.register(Aula)
admin.site.register(Inscricao)
admin.site.register(Treino)

