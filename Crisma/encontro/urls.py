from django.urls import path
from .views import encontroHome, cadastrarEncontro, listaPresenca, listarEncontros

urlpatterns = [
    path('', encontroHome, name='encontro'),
    path('cadastrarEncontro',cadastrarEncontro, name='cadEncontro'),
    path('listapresenca/', listaPresenca, name='listaPresenca'),
    path('listarEncontros', listarEncontros, name='listarEncontros')
]