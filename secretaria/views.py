from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'secretaria/home.html', context = context)

def dados(request):
    context = {}
    return render(request, 'secretaria/dados.html', context = context)