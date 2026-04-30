from pprint import pprint
from typing import Iterable

from django.utils.text import slugify

from nucleo.algorithm import CIDADES, ROTAS
from nucleo.models import City, Route


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
