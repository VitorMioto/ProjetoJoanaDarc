from django.forms import ModelForm
from .models import Crismando

class CrismandoForm(ModelForm):
    class Meta():
        model = Crismando
        fields=['nome','dtNascimento','endereco',
                'numero','compl','nomeMae','nomePai',
                'telMae','telPai','fezBatismo','fezComunhao', 'turma']