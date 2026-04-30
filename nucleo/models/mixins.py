from typing import Iterable

from ..algoritmos.interfaces import ICidade, IRotas


class CidadeMixin(ICidade):
    @property
    def importancia(self) -> int:
        return self.importance

    @property
    def vizinhos(self) -> Iterable[IRotas]:
        return self.routes.through.objects.all()


class RotasMixin(IRotas):
    @property
    def origem(self) -> ICidade:
        return self.src

    @property
    def destino(self) -> ICidade:
        return self.dest

    @property
    def custo(self) -> float:
        return float(self.cost)

    @property
    def tempo(self) -> int:
        return self.time
