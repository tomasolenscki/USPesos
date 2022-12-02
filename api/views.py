from rest_framework import generics
from professores.models import Exercicio
from .serializers import ExercicioSerializer

class ExercicioList(generics.ListCreateAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer

class ExercicioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer