from django import forms

from ..algorithm import CIDADES


def _get_choices_cidades() -> list[tuple[str, str]]:
    # (key para o select, label para o usuário)
    return [(cidade, cidade) for cidade in CIDADES.keys()]


class PlanejadorForm(forms.Form):
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
