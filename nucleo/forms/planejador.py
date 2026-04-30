from django import forms

from ..algoritmos import ALGORITMOS_CHOICES
from ..models import City


def _get_choices_cidades() -> list[tuple[str, str]]:
    # (key para o select, label para o usuário)
    return [(cidade.slug, cidade.name) for cidade in City.objects.all()]


class PlanejadorForm(forms.Form):
    algoritmo = forms.ChoiceField(
        choices=ALGORITMOS_CHOICES,
        label='Perfil de priorização',
        help_text='Define qual atributo será priorizado na estratégia'
    )
    origem = forms.ChoiceField(
        choices=_get_choices_cidades,
        label='Cidade de Origem'
    )
    tempo_maximo = forms.IntegerField(
        min_value=0,
        initial=40,
        label='Tempo Máximo (Horas)',
    )
    orcamento_maximo = forms.DecimalField(
        min_value=0,
        decimal_places=2,
        initial=100,
        label='Orçamento (R$)',
    )
