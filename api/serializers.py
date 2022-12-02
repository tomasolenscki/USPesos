from rest_framework import serializers
from professores.models import Exercicio


class ExercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercicio
        fields = ['id', 'nome', 'urlfoto', 'maquina']