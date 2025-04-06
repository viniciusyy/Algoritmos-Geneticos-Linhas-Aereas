# Algoritmos Genéticos - Linhas Aéreas

Este projeto implementa um algoritmo genético para otimização da alocação de voos em uma companhia aérea. O objetivo é minimizar conflitos de horários e o uso excessivo de aeronaves, utilizando operadores clássicos dos algoritmos genéticos como seleção, mutação e cross-over.

## Funcionalidades

- **Exibição do Resultado Final:** Ao término da execução, o algoritmo exibe a melhor solução encontrada, mostrando o fitness e a alocação dos voos.
- **Função de Seleção:** Combina a população atual com indivíduos gerados por mutação e cross-over, selecionando os mais aptos para a próxima geração.
- **Função de Mutação:** Gera variações aleatórias no cromossomo de cada indivíduo, permitindo a exploração do espaço de soluções.
- **Função de Cross-Over:** Realiza o cruzamento de dois indivíduos, combinando seus cromossomos para gerar novos indivíduos.
- **Representação do Espaço de Estados:** Cada indivíduo é representado por um cromossomo (lista) onde cada gene indica o avião atribuído a um voo específico.

## Estrutura do Projeto

- **`algoritmo_genetico.py`:** Gerencia o loop evolutivo do algoritmo genético, controla gerações e critérios de parada.
- **`individuo.py`:** Define o modelo de indivíduo, incluindo o cromossomo, a função fitness e os operadores de mutação e cross-over.
- **`populacao.py`:** Implementa a geração inicial da população e as funções de mutação, crossover e seleção.
- **`main.py`:** Arquivo principal que configura os voos, os parâmetros do algoritmo e inicia a execução.

## Pré-requisitos

- Python 3.6 ou superior
- Numpy

