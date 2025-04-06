from individuo import Individuo
import random

class Populacao:
    """
    Representa a população de indivíduos.
    """

    def __init__(self, voos, tamanho_populacao=10, num_avioes=10):
        self.voos = voos
        self.tamanho_populacao = tamanho_populacao
        self.num_avioes = num_avioes
        self.populacao = []
        self.inicializacao()

    def inicializacao(self):
        """
        Inicializa a população com indivíduos aleatórios.
        """
        for _ in range(self.tamanho_populacao):
            ind = Individuo(self.voos, self.num_avioes)
            self.populacao.append(ind)

    def mutacao(self):
        """
        Aplica mutação em todos os indivíduos da população,
        retornando uma nova lista de indivíduos.
        """
        nova_lista = []
        for individuo in self.populacao:
            nova_lista.append(individuo.mutacao())
        return nova_lista

    def crossover(self):
        """
        Faz cruzamento em pares na população,
        retornando uma nova lista de indivíduos (filhos).
        """
        nova_lista = []
        # Cruzamento simples em pares: (0,1), (2,3), ...
        for i in range(0, self.tamanho_populacao, 2):
            if i + 1 < self.tamanho_populacao:
                pai = self.populacao[i]
                mae = self.populacao[i + 1]
                filho1, filho2 = pai.crossover(mae)
                nova_lista.append(filho1)
                nova_lista.append(filho2)
            else:
                # Se sobrar 1 no final, não faz crossover
                nova_lista.append(self.populacao[i])
        return nova_lista

    def selecionar(self, populacao_mutada, populacao_crossover):
        """
        Combina a população atual com as populações mutadas e de crossover,
        e então seleciona os melhores (com maior fitness).
        """
        # Unir todos
        self.populacao.extend(populacao_mutada)
        self.populacao.extend(populacao_crossover)

        # Ordenar pela aptidão (fitness) em ordem decrescente
        self.populacao.sort(key=lambda ind: ind.fitness(), reverse=True)

        # Cortar para manter só os melhores
        self.populacao = self.populacao[:self.tamanho_populacao]

    def top_fitness(self):
        return self.populacao[0].fitness()

    def top_individuo(self):
        return self.populacao[0]
