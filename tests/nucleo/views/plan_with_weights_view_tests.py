from http import HTTPStatus

from django.shortcuts import resolve_url
from django.template.response import TemplateResponse
from django.test import Client
from pytest import fixture, mark

from nucleo.tests.seeds.cidades_e_rotas import tres_cidades

pytestmark = mark.django_db


@fixture(autouse=True)
def setup_cidades(db):
    return tres_cidades()


@fixture(scope='module')
def url_view():
    return resolve_url('index_peso')



def test_get_view(client: Client, url_view):
    response = client.get(url_view)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)
    assert 'Resultado do Algoritmo' not in response.text
    assert response.context_data is not None
    assert 'form' in response.context_data


def test_submit_form(client: Client, url_view):
    data = {
        'peso_importancia': 0.5,
        'peso_custo': 0.01,
        'peso_tempo': 0.5,
        'origem': 'a',
        'tempo_maximo': 10,
        'orcamento_maximo': 300,
    }
    response = client.post(url_view, data)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)
    assert response.is_rendered
    assert response.context_data is not None
    assert 'form' in response.context_data
    assert response.context_data['form'].is_valid()
    assert 'resultado' in response.context_data
    assert 'Resultado do Algoritmo' in response.text


def test_post_form_invalid(client: Client, url_view):
    '''Test form inválido deve devolver mensagem de erro nos campos'''
    data = {
        'peso_importancia': 0.5,
        'peso_custo': 0.01,
        'peso_tempo': 5,
        'origem': 'a',
        'tempo_maximo': 10,
        'orcamento_maximo': -2,
    }
    response = client.post(url_view, data)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)
    assert response.context_data is not None and 'form' in response.context_data
    form = response.context_data['form']
    assert form.is_valid() is False
    assert len(form.errors) == 2
