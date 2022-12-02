from django.urls import path
from .views import ExercicioList, ExercicioDetail

urlpatterns = [
    path('exercicios/<int:pk>/', ExercicioDetail.as_view()),
    path('exercicios/', ExercicioList.as_view())
]