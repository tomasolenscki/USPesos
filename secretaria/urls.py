from django.urls import path
from . import views

# URLs dos usuários

app_name = 'secretaria'

urlpatterns = [
    path('home/',views.home, name = 'home'),
    path('dados/',views.dados, name = 'dados'),
]