from pprint import pprint
from typing import Iterable

from django.utils.text import slugify

from nucleo.models import City, Route

CIDADES = {
    'São Paulo': {'importancia': 8},
    'Rio de Janeiro': {'importancia': 10},
    'Belo Horizonte': {'importancia': 7},
    'Curitiba': {'importancia': 6},
    'Florianópolis': {'importancia': 9},
}

ROTAS = {
    'São Paulo': {
        'Rio de Janeiro': {'custo': 150, 'tempo': 6},
        'Belo Horizonte': {'custo': 120, 'tempo': 8},
        'Curitiba': {'custo': 100, 'tempo': 5}
    },
    'Rio de Janeiro': {
        'São Paulo': {'custo': 150, 'tempo': 6},
        'Belo Horizonte': {'custo': 180, 'tempo': 7}
    },
    'Belo Horizonte': {
        'São Paulo': {'custo': 120, 'tempo': 8},
        'Rio de Janeiro': {'custo': 180, 'tempo': 7}
    },
    'Curitiba': {
        'São Paulo': {'custo': 100, 'tempo': 5},
        'Florianópolis': {'custo': 80, 'tempo': 4}
    },
    'Florianópolis': {
        'Curitiba': {'custo': 80, 'tempo': 4}
    }
}


def create_cities_if_empty(cidades: dict[str, dict[str, int]] = CIDADES):
    if City.objects.first() is None:
        return City.objects.bulk_create([
            City(slug=slugify(cidade), name=cidade, importance=item['importancia'])
            for cidade, item in cidades.items()
        ])


def create_routes_if_empty(
        cities: Iterable[City],
        routes: dict[str, dict[str, dict[str, int]]] = ROTAS
        ):
    if Route.objects.first() is None:
        created_map = {c.name: c for c in cities}
        created = []

        for cidade, city_instance in created_map.items():
            created_routes = Route.objects.bulk_create([
                Route(
                    src=city_instance, dest=created_map[dest],
                    cost=attrs['custo'], time=attrs['tempo'],
                )
                for dest, attrs in routes[cidade].items()
            ])
            created.extend(created_routes)
        return created

def populate_db():
    cidades = create_cities_if_empty()
    print('Cidades criadas:')
    pprint(cidades)
    cidades = cidades or City.objects.all()

    rotas = create_routes_if_empty(cidades)
    print('Rotas Criadas:')
    pprint(rotas)


def tres_cidades() -> list[City]:
    cidades = City.objects.bulk_create([
        City(slug='a', name='A'),
        City(slug='b', name='B'),
        City(slug='c', name='C', importance=10),
    ])
    Route.objects.bulk_create([
        Route(src=cidades[0], dest=cidades[1], cost=100, time=2),  # A -> B
        Route(src=cidades[0], dest=cidades[2], cost=100, time=2),  # A -> C
        Route(src=cidades[1], dest=cidades[2], cost=100, time=2),  # B -> C
    ])
    return cidades


def uma_cidade() -> list[City]:
    return [City.objects.create(slug='a', name='A')]


def cidades_sem_rotas() -> list[City]:
    return City.objects.bulk_create([
        City(slug='a', name='A'),
        City(slug='b', name='B'),
        City(slug='c', name='C', importance=10),
    ])


def cidades_sem_rotas_saindo():
    cidades = City.objects.bulk_create([
        City(slug='a', name='A'),
        City(slug='b', name='B'),
        City(slug='c', name='C', importance=10),
    ])
    Route.objects.bulk_create([
        Route(src=cidades[1], dest=cidades[2], cost=100, time=2),  # B -> C
        Route(src=cidades[2], dest=cidades[1], cost=100, time=2),  # C -> B
        Route(src=cidades[1], dest=cidades[0], cost=100, time=2),  # B -> A
        Route(src=cidades[2], dest=cidades[0], cost=100, time=2),  # C -> A
    ])
    return cidades
