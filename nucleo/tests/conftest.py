# Configure fixtures gerais aqui para serem usadas nos testes em subpastas
import pytest

from .seeds.cidades_e_rotas import populate_db


@pytest.fixture(scope='session')
def cidades_setup(django_db_setup):
    populate_db()
