
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

def planejar_rota_gulosa(origem, tempo_maximo, orcamento_maximo):
    
    cidade_atual = origem
    visitadas = [cidade_atual]
    tempo_gasto = 0
    dinheiro_gasto = 0
    satisfacao_total = CIDADES[origem]['importancia']
    detalhes_viagem = []

    
    peso_importancia = 1.0
    peso_custo = 0.01  
    peso_tempo = 0.5

    while True:
        melhor_proxima = None
        maior_utilidade = -float('inf')
        melhor_rota = None

        
        vizinhos = ROTAS.get(cidade_atual, {})
        
        for vizinho, dados_rota in vizinhos.items():
            if vizinho not in visitadas:
                custo = dados_rota['custo']
                tempo = dados_rota['tempo']
                                
                if (dinheiro_gasto + custo <= orcamento_maximo) and (tempo_gasto + tempo <= tempo_maximo):
                    importancia = CIDADES[vizinho]['importancia']
                                       
                    utilidade = (peso_importancia * importancia) - (peso_custo * custo) - (peso_tempo * tempo)
                    
                    if utilidade > maior_utilidade:
                        maior_utilidade = utilidade
                        melhor_proxima = vizinho
                        melhor_rota = dados_rota
            
        if not melhor_proxima:
            break
            
        visitadas.append(melhor_proxima)
        tempo_gasto += melhor_rota['tempo']
        dinheiro_gasto += melhor_rota['custo']
        satisfacao_total += CIDADES[melhor_proxima]['importancia']
        
        detalhes_viagem.append({
            'de': cidade_atual,
            'para': melhor_proxima,
            'tempo': melhor_rota['tempo'],
            'custo': melhor_rota['custo']
        })
        
        cidade_atual = melhor_proxima
        
    return {
        'rota': visitadas,
        'detalhes': detalhes_viagem,
        'tempo_total': tempo_gasto,
        'custo_total': dinheiro_gasto,
        'satisfacao_total': satisfacao_total
    }