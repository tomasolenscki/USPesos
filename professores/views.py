from django.shortcuts import render
from django.http import HttpResponse

# Create your models here.

def home(request):
    context = {}
    return render(request, 'professores/home.html', context = context)
