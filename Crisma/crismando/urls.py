from django.urls import path
from .views import novoCrismando, novaTurma,listaPresenca

urlpatterns = [
    path('',novoCrismando, name='crismando'),
    path('novaturma/', novaTurma, name='novaTurma'),
    path('listapresenca/', listaPresenca, name='listaPresenca')
]