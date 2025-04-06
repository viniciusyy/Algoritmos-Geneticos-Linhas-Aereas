class AlgoritmoGeneticoPopulacao:
    """
    Classe que gerencia o loop de evolução do Algoritmo Genético.
    """

    def __init__(self, populacao):
        self.populacao = populacao
        self.erro = float('inf')
        self.geracoes = 1

    def erro_final(self):
        return self.erro

    def qtd_geracoes(self):
        return self.geracoes

    def rodar(self, max_geracoes=1000, imprimir_em_geracaoes=100, erro_min=0.0001):
        """
        Executa o loop principal do AG.
        - Em cada geração, gera mutações e crossovers
        - Seleciona os melhores
        - Avalia se o erro (1 - fitness) está abaixo de um limiar
        """

        # Imprime primeira geração
        fitness_inicial = self.populacao.top_fitness()
        self.erro = (1 - fitness_inicial)
        print(f"Geração: {self.geracoes}, Erro: {round(self.erro, 6)}")
        # Opcional: imprimir a alocação inicial
        # print(self.populacao.top_individuo().imprime())

        while True:
            if self.geracoes >= max_geracoes or self.erro <= erro_min:
                # Chegamos ao fim
                print(f"Geração: {self.geracoes}, Erro: {round(self.erro, 6)}")
                break

            # Cria novas populações
            populacao_mutada = self.populacao.mutacao()
            populacao_crossover = self.populacao.crossover()

            # Seleciona os melhores
            self.populacao.selecionar(populacao_mutada, populacao_crossover)

            # Atualiza erro
            melhor_fitness = self.populacao.top_fitness()
            self.erro = (1 - melhor_fitness)

            self.geracoes += 1
            if self.geracoes % imprimir_em_geracaoes == 0:
                print(f"Geração: {self.geracoes}, Erro: {round(self.erro, 6)}")

        # Retorna o melhor indivíduo ao final
        return self.populacao.top_individuo()
