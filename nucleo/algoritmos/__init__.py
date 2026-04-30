# Registre os algoritmos aqui
from .guloso import AlgoritmoGuloso
from .interfaces import BaseAlgoritmo

ALGORITMOS_CHOICES: dict[str, BaseAlgoritmo] = {
    'importancia': AlgoritmoGuloso(),
}
