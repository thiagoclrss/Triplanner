from django.shortcuts import get_object_or_404
from django.views.generic import FormView

from nucleo.models import City

from ..algoritmos.guloso import AlgoritmoGuloso
from ..forms.planos_e_pesos import PesosPlanosForm


class PlanWithWeightsFormView(FormView):
    template_name = 'nucleo/index.html'
    form_class = PesosPlanosForm

    def form_valid(self, form: PesosPlanosForm):
        origem = form.cleaned_data.get('origem')
        cidade = get_object_or_404(City, slug=origem)

        tempo_maximo = form.cleaned_data.get('tempo_maximo', 0)
        orcamento_maximo = form.cleaned_data.get('orcamento_maximo', 0)
        importancia = form.cleaned_data.get('peso_importancia', 0)
        custo = form.cleaned_data.get('peso_custo', 0)
        tempo = form.cleaned_data.get('peso_tempo', 0)
        resultado = AlgoritmoGuloso(importancia, custo, tempo).planejar(cidade, tempo_maximo, orcamento_maximo)

        contexto = self.get_context_data(form=form)
        contexto['resultado'] = resultado
        return self.render_to_response(contexto)

