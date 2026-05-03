from http import HTTPStatus

import pytest
from django.template.response import TemplateResponse
from django.test import Client
from django.forms import Form

pytestmark = pytest.mark.django_db

def test_get_template(client: Client, django_db_setup):
    """Test não deve vir card de resultados em GET"""
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)
    assert 'Resultado do Algoritmo' not in response.text
    assert response.context_data is not None
    assert 'form' in response.context_data
    assert 'resultado' not in response.context_data

def test_post_template(client: Client, django_db_setup):
    """Test deve devolver resultado"""
    data = {
        'algoritmo': 'importancia',
        'origem': 'sao-paulo',
        'tempo_maximo': 40,
        'orcamento_maximo': 150.55,
    }
    response = client.post('/', data=data)

    assert response.status_code == HTTPStatus.OK
    assert isinstance(response, TemplateResponse)
    assert response.is_rendered
    assert 'Resultado do Algoritmo' in response.text
    assert response.context_data is not None
    assert 'form' in response.context_data
    assert 'resultado' in response.context_data


def test_post_template_invalido(client: Client, django_db_setup):
    """Form inválido deve devolver erros"""
    invalid_data = {
        'algoritmo': 'inexistente',
        'origem': 'A',
        'tempo_maximo': -1,
    }
    response = client.post('/', data=invalid_data)

    assert isinstance(response, TemplateResponse)
    assert response.status_code == HTTPStatus.OK
    assert 'Resultado do Algoritmo' not in response.text
    assert response.context_data is not None
    assert 'form' in response.context_data
    assert isinstance(form := response.context_data['form'], Form)
    assert form.is_valid() is False
    assert len(form.errors) > 0
