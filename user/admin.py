from django.contrib import admin
from .models import User, Aluno, Professor

# Register your models here.

admin.site.register(User)
admin.site.register(Aluno)
admin.site.register(Professor)
