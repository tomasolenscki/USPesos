from django.contrib import admin
from .models import User, Aluno, Professor, Secretario

# Register your models here.

admin.site.register(User)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Secretario)
