from django.shortcuts import render
from .algorithm import planejar_rota_gulosa, CIDADES

def index(request):
    contexto = {
        'cidades_disponiveis': CIDADES.keys()
    }

    if request.method == 'POST':
        origem = request.POST.get('origem')
        tempo_maximo = int(request.POST.get('tempo_maximo'))
        orcamento_maximo = float(request.POST.get('orcamento_maximo'))

        resultado = planejar_rota_gulosa(origem, tempo_maximo, orcamento_maximo)
        
        contexto['resultado'] = resultado
        contexto['dados_form'] = {
            'origem': origem,
            'tempo_maximo': tempo_maximo,
            'orcamento_maximo': orcamento_maximo
        }

    return render(request, 'nucleo/index.html', contexto)