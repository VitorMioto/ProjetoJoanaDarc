from django.urls import path
from .views import novoCrismando, novaTurma

urlpatterns = [
    path('',novoCrismando, name='crismando'),
    path('novaturma/', novaTurma, name='novaTurma'),
    #path('listarturma/',listarTurma,name='listarTurma'),
]