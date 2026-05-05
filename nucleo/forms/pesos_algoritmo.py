from django import forms


class RangeInput(forms.NumberInput):
    input_type = 'range'
    template_name = 'base/widgets/range_field.html'


class PesosAlgoritmoForm(forms.Form):
    peso_importancia = forms.FloatField(
        max_value=1, min_value=0, step_size=0.1,
        initial=1, widget=RangeInput,
        label='Peso importância'
    )
    peso_custo = forms.FloatField(
        max_value=1, min_value=0, step_size=0.01,
        initial=0.01, widget=RangeInput
    )
    peso_tempo = forms.FloatField(
        max_value=1, min_value=0, step_size=0.1,
        initial=0.5, widget=RangeInput
    )
