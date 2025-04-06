from populacao import Populacao
from algoritmo_genetico import AlgoritmoGeneticoPopulacao

def criar_voos():
    """
    Cria uma lista de dicionários com informações de cada voo.
    Cada voo terá:
      - origem
      - destino
      - partida (hora do dia, ex: 6.0 = 6h da manhã)
      - chegada (partida + tempo_de_voo)
      - duracao
    Para simplificar, vamos distribuir as partidas de forma linear ao longo do dia.
    """

    # Tabela das rotas
    # (origem, destino, tempo_voo, num_voos)
    rotas = [
        ("GRU", "GIG", 1.0, 10),
        ("GRU", "BSB", 2.0, 6),
        ("GRU", "CNF", 1.5, 8),
        ("GIG", "GRU", 1.0, 10),
        ("GIG", "BSB", 2.0, 5),
        ("GIG", "CNF", 1.5, 6),
        ("BSB", "GRU", 2.0, 6),
        ("BSB", "GIG", 2.0, 5),
        ("BSB", "CNF", 1.5, 7),
        ("CNF", "GRU", 1.5, 8),
        ("CNF", "GIG", 1.5, 6),
        ("CNF", "BSB", 1.5, 7),
    ]

    voos = []
    # Vamos supor que os voos estão distribuídos entre 6h e 22h
    for (origem, destino, tempo, qtd) in rotas:
        intervalo = 16.0  # 6h -> 22h = 16 horas de janela
        if qtd == 1:
            # Se só tem 1 voo, bota no meio do dia
            partida = 6.0 + intervalo / 2.0
            chegada = partida + tempo
            voos.append({
                'origem': origem,
                'destino': destino,
                'partida': partida,
                'chegada': chegada,
                'duracao': tempo
            })
        else:
            # Distribui voos igualmente
            espaco = intervalo / (qtd - 1)
            for i in range(qtd):
                partida = 6.0 + i * espaco
                chegada = partida + tempo
                voos.append({
                    'origem': origem,
                    'destino': destino,
                    'partida': partida,
                    'chegada': chegada,
                    'duracao': tempo
                })

    return voos

def main():
    voos = criar_voos()

    TAMANHO_POPULACAO = 20
    NUM_AVIOES = 15  # limite máximo de aviões que podemos usar

    populacao_inicial = Populacao(voos, tamanho_populacao=TAMANHO_POPULACAO, num_avioes=NUM_AVIOES)

    ag = AlgoritmoGeneticoPopulacao(populacao_inicial)

    melhor_individuo = ag.rodar(
        max_geracoes=1000,
        imprimir_em_geracaoes=100,
        erro_min=0.0001
    )

    print("Melhor Solução encontrada:")
    print(f"Fitness: {melhor_individuo.fitness()}")
    print(melhor_individuo.imprime())

if __name__ == "__main__":
    main()
