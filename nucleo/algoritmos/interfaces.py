from dataclasses import dataclass
from typing import Iterable


@dataclass
class Resposta:
    rota: list[ICidade]
    detalhes: list[IRotas]
    tempo_total: int
    custo_total: float
    satisfacao_total: int


class ICidade:
    def __str__(self) -> str: raise NotImplementedError()

    @property
    def importancia(self) -> int: raise NotImplementedError()

    @property
    def vizinhos(self) -> Iterable[IRotas]: raise NotImplementedError()


class IRotas:
    def __str__(self) -> str: raise NotImplementedError()

    @property
    def origem(self) -> ICidade: raise NotImplementedError()

    @property
    def destino(self) -> ICidade: raise NotImplementedError()

    @property
    def custo(self) -> float: raise NotImplementedError()

    @property
    def tempo(self) -> int: raise NotImplementedError()


class BaseAlgoritmo:
    def planejar(
            self, 
            origem: ICidade,
            tempo_maximo: int,
            orcamento_maximo: float
        ) -> Resposta:
        raise NotImplementedError()

    def __str__(self) -> str:
        return 'Algoritmo Base para planejar rota'

    def description(self) -> str:
        return ''
