from django.shortcuts import get_object_or_404
from django.views.generic import FormView

from ..algoritmos import ALGORITMOS_CHOICES
from ..forms.planejador import PlanejadorForm
from ..models import City


class PlanFormView(FormView):
    template_name = 'nucleo/index.html'
    form_class = PlanejadorForm

    def form_valid(self, form: PlanejadorForm):
        algoritmo_choice = form.cleaned_data.get('algoritmo')
        origem = form.cleaned_data.get('origem')
        tempo_maximo = form.cleaned_data.get('tempo_maximo')
        orcamento_maximo = form.cleaned_data.get('orcamento_maximo')

        cidade = get_object_or_404(City, slug=origem)
        algoritmo = ALGORITMOS_CHOICES[algoritmo_choice]
        resultado = algoritmo.planejar(cidade, tempo_maximo, orcamento_maximo)

        contexto = self.get_context_data(form=form)
        contexto['resultado'] = resultado
        return self.render_to_response(contexto)
