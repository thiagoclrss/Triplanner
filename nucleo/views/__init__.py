from django.views.generic import FormView

from ..algorithm import CIDADES, planejar_rota_gulosa
from ..forms.planejador import PlanejadorForm


class PlanFormView(FormView):
    template_name = 'nucleo/index.html'
    form_class = PlanejadorForm

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['cidades_disponiveis'] = CIDADES.keys()
        return context

    def form_valid(self, form: PlanejadorForm):
        origem = form.cleaned_data.get('origem')
        tempo_maximo = form.cleaned_data.get('tempo_maximo')
        orcamento_maximo = form.cleaned_data.get('orcamento_maximo')
        resultado = planejar_rota_gulosa(origem, tempo_maximo, orcamento_maximo)

        contexto = self.get_context_data(form=form)
        contexto['resultado'] = resultado
        return self.render_to_response(contexto)
