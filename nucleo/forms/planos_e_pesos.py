from .pesos_algoritmo import PesosAlgoritmoForm
from .planejador import PlanejadorForm


class PesosPlanosForm(PlanejadorForm, PesosAlgoritmoForm):
    algoritmo = None
