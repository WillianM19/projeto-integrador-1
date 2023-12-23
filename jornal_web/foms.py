from django.forms import ModelForm
from .models import Publicacao

class PublicacaoForm(ModelForm):
    class Meta:
        model = Publicacao
        fields = ['conteudo']
        labels = {
            'conteudo': '',
        }