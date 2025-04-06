import random
import math

class Individuo:
    """
    Cada indivíduo representa uma alocação de voos para aviões.
    O cromossomo é uma lista em que cada posição representa um voo
    e o valor nessa posição representa o ID do avião alocado.
    """

    def __init__(self, voos, num_avioes=10, cromossomo=None):
        """
        :param voos: lista de dicionários com informações de cada voo.
        :param num_avioes: número máximo de aviões que podemos usar.
        :param cromossomo: lista de atribuição (voo -> avião).
        """
        self.voos = voos
        self.num_avioes = num_avioes

        if cromossomo is None:
            # Inicializa o cromossomo aleatoriamente
            self.cromossomo = [
                random.randint(0, self.num_avioes - 1) for _ in range(len(self.voos))
            ]
        else:
            self.cromossomo = cromossomo

        self._fitness_cache = None  # Cache para o valor do fitness

    def fitness(self):
        """
        Calcula a adequação (fitness) do indivíduo.
        - Penaliza conflitos de horário para o mesmo avião.
        - Penaliza o uso de muitos aviões.
        - Tenta minimizar o número total de aviões utilizados.

        Estratégia de cálculo:
          fitness = 1 / (1 + num_avioes_usados + 100 * conflitos)
        Quanto MAIOR o fitness, melhor.
        """
        if self._fitness_cache is not None:
            return self._fitness_cache

        # Agrupar voos por avião
        avioes_voos = {}
        for idx_voo, id_aviao in enumerate(self.cromossomo):
            if id_aviao not in avioes_voos:
                avioes_voos[id_aviao] = []
            avioes_voos[id_aviao].append(self.voos[idx_voo])

        # Calcular conflitos
        # Conflito ocorre se dois voos do mesmo avião se sobrepõem no tempo,
        # considerando 1h antes do voo (preparação) e 0.5h depois (manutenção).
        conflitos = 0
        for id_aviao, lista_voos in avioes_voos.items():
            # Ordena os voos por horário de partida
            lista_voos_ordenada = sorted(lista_voos, key=lambda v: v['partida'])
            for i in range(len(lista_voos_ordenada) - 1):
                voo_atual = lista_voos_ordenada[i]
                proximo_voo = lista_voos_ordenada[i + 1]
                fim_voo_atual = voo_atual['chegada'] + 0.5  # 0.5h pós-voo
                inicio_proximo_voo = proximo_voo['partida'] - 1.0  # 1h preparação
                if fim_voo_atual > inicio_proximo_voo:
                    conflitos += 1

        # Quantos aviões foram efetivamente usados
        avioes_usados = set(self.cromossomo)
        num_avioes_usados = len(avioes_usados)

        # Função de fitness: penaliza uso de aviões e conflitos
        self._fitness_cache = 1.0 / (1.0 + num_avioes_usados + 100.0 * conflitos)
        return self._fitness_cache

    def mutacao(self, taxa_mutacao=0.1):
        """
        Cria e retorna um novo indivíduo (cópia) com mutação.
        Para cada gene, há uma chance 'taxa_mutacao' de atribuir outro avião aleatório.
        """
        novo_cromossomo = self.cromossomo[:]
        for i in range(len(novo_cromossomo)):
            if random.random() < taxa_mutacao:
                novo_cromossomo[i] = random.randint(0, self.num_avioes - 1)
        return Individuo(self.voos, self.num_avioes, cromossomo=novo_cromossomo)

    def crossover(self, outro):
        """
        Realiza o cruzamento de um ponto com outro indivíduo.
        Gera dois novos indivíduos.
        """
        corte = random.randint(1, len(self.cromossomo) - 1)
        filho1_crom = self.cromossomo[:corte] + outro.cromossomo[corte:]
        filho2_crom = outro.cromossomo[:corte] + self.cromossomo[corte:]
        filho1 = Individuo(self.voos, self.num_avioes, cromossomo=filho1_crom)
        filho2 = Individuo(self.voos, self.num_avioes, cromossomo=filho2_crom)
        return filho1, filho2

    def imprime(self):
        """
        Retorna uma string com a visualização do cromossomo:
        - Exibe quais voos e qual avião foi alocado.
        - Os horários são formatados no padrão HH:MM.
        """
        def format_time(t):
            # Normaliza o horário para o padrão 24h
            t = t % 24
            hours = int(t)
            minutes = int(round((t - hours) * 60))
            if minutes == 60:
                hours = (hours + 1) % 24
                minutes = 0
            return f"{hours:02d}:{minutes:02d}"
        
        # Organiza as alocações por avião para melhor visualização
        alocacoes = list(zip(self.cromossomo, self.voos))
        alocacoes.sort(key=lambda x: x[0])
        
        s = "Alocação de Aviões (avião -> [voos]):\n"
        aviao_atual = None
        for id_aviao, voo in alocacoes:
            if id_aviao != aviao_atual:
                s += f"\n  Avião {id_aviao}:\n"
                aviao_atual = id_aviao
            partida = format_time(voo['partida'])
            chegada = format_time(voo['chegada'])
            s += (f"    {voo['origem']} -> {voo['destino']} | "
                  f"Partida: {partida} | Chegada: {chegada}\n")
        return s
