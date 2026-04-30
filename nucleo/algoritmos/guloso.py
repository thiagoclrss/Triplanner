from .interfaces import BaseAlgoritmo, ICidade, Resposta


class AlgoritmoGuloso(BaseAlgoritmo):
    def __init__(self) -> None:
        self.peso_importancia = 1.0
        self.peso_custo = 0.01  
        self.peso_tempo = 0.5

    def __str__(self) -> str:
        return 'Importância'
    
    def description(self) -> str:
        return ('Perfil que considera mais a importância da cidade')

    def utilidade(self, importancia, custo, tempo) -> float:
        return (
            (self.peso_importancia * importancia)
            - (self.peso_custo * custo)
            - (self.peso_tempo * tempo)
        )

    def planejar(self, origem: ICidade, tempo_maximo: int, orcamento_maximo: float) -> Resposta:

        cidade_atual = origem
        visitadas = [cidade_atual]
        tempo_gasto = 0
        dinheiro_gasto = 0
        satisfacao_total = origem.importancia
        detalhes_viagem = []

        while True:
            maior_utilidade = -float('inf')
            melhor_proxima = None
            melhor_rota = None

            vizinhos = cidade_atual.vizinhos

            for rota in vizinhos:
                vizinho = rota.destino
                if vizinho not in visitadas:
                    custo = rota.custo
                    tempo = rota.tempo
                    importancia = cidade_atual.importancia

                    if (dinheiro_gasto + custo <= orcamento_maximo) and (tempo_gasto + tempo <= tempo_maximo):
                        utilidade = self.utilidade(importancia, custo, tempo)

                        if utilidade > maior_utilidade:
                            maior_utilidade = utilidade
                            melhor_proxima = vizinho
                            melhor_rota = rota

            if melhor_proxima is None:
                break

            # assert melhor_rota is not None

            visitadas.append(melhor_proxima)
            tempo_gasto += melhor_rota.tempo
            dinheiro_gasto += melhor_rota.custo
            satisfacao_total += melhor_proxima.importancia

            detalhes_viagem.append(melhor_rota)

            cidade_atual = melhor_proxima

        return Resposta(
            rota=visitadas,
            detalhes=detalhes_viagem,
            tempo_total=tempo_gasto,
            custo_total=dinheiro_gasto,
            satisfacao_total=satisfacao_total
        )
