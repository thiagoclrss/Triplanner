# Configure fixtures gerais aqui para serem usadas nos testes em subpastas
import pytest

from nucleo.tests.seeds.cidades_e_rotas import populate_db


@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        populate_db()
