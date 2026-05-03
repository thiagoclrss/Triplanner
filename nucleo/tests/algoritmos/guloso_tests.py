import pytest

from nucleo.algoritmos.guloso import AlgoritmoGuloso, BaseAlgoritmo
from nucleo.models import City

from ..seeds import cidades_e_rotas as seed


@pytest.fixture(params=(AlgoritmoGuloso,))
def algoritmo(request) -> type[BaseAlgoritmo]:
    return request.param


def test_escolha_por_importancia(db, algoritmo):
    '''Testa com 3 cidades, as duas rotas que partem do início são iguais em
    custo e tempo, a única diferença é a importância da cidade. (C > B)
    '''
    cidades = seed.tres_cidades()
    inicio = cidades[0]  # A

    resposta = algoritmo().planejar(inicio, 10, 200)

    # unica rota possível deve ser A -> B
    assert len(resposta.rota) == 2

    origem, destino = resposta.rota
    assert origem.nome == 'A'
    assert destino.nome == 'C'
    assert len(resposta.detalhes) == 1
    assert resposta.detalhes[0].origem.pk == 'a'
    assert resposta.detalhes[0].destino.pk == 'c'


@pytest.mark.parametrize('gerar_cidades', (seed.uma_cidade, seed.cidades_sem_rotas, seed.cidades_sem_rotas_saindo))
def test_rota_impossivel(db, gerar_cidades, algoritmo):
    '''Testa configurações nas quais deve ser impossível gerar rotas, pois
    não há caminho possível partindo da cidade A
    '''
    cidades = gerar_cidades()
    inicio = cidades[0]

    resposta = algoritmo().planejar(inicio, 10, 200)

    assert len(resposta.rota) == 1
    assert len(resposta.detalhes) == 0
    assert resposta.rota[0].nome == 'A'


def test_custo_e_tempo_baixos(db, algoritmo):
    '''Testa se o custo for muito baixo, não será possível formar rotas'''
    cidades = seed.tres_cidades()
    inicio = cidades[0]  # A

    resposta = algoritmo().planejar(inicio, 1, 50)

    assert len(resposta.rota) == 1
    assert len(resposta.detalhes) == 0
    assert resposta.rota[0].nome == 'A'
