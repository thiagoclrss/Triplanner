from http import HTTPStatus

import pytest
from django.template.response import TemplateResponse
from django.test import Client

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
