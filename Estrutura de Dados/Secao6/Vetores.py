import numpy as np
import random
import time


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultimaPosicao == -1:
            print("Vetor está vazio")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, " - ", self.valores[i])

    def insere(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
            return

        posicao = 0
        for i in range(self.ultimaPosicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultimaPosicao:
                posicao = i + 1

        x = self.ultimaPosicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = valor
        self.ultimaPosicao += 1

    def pesquisa(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if self.valores[i] == valor:
                return i
        return -1

    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultimaPosicao

        while limite_inferior <= limite_superior:
            posicao_atual = (limite_inferior + limite_superior) // 2

            if self.valores[posicao_atual] == valor:
                return posicao_atual
            elif self.valores[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
            else:
                limite_superior = posicao_atual - 1

        return -1

    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao -= 1


class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    def imprime(self):
        if self.ultimaPosicao == -1:
            print("Vetor está vazio")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, " - ", self.valores[i])

    def insere(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
            return
        self.ultimaPosicao += 1
        self.valores[self.ultimaPosicao] = valor

    def pesquisa(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if self.valores[i] == valor:
                return i
        return -1

    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao -= 1


# Comparativo de desempenho
def comparar_operacoes(tamanho, valor_procurado):
    print(f"\n--- Comparando operações para {tamanho} elementos ---")

    # Gerar lista aleatória
    lista_aleatoria = [random.randint(1, 10000) for _ in range(tamanho)]

    # Vetor Ordenado
    vetor_ordenado = VetorOrdenado(tamanho)
    start = time.time()
    for valor in lista_aleatoria:
        vetor_ordenado.insere(valor)
    tempo_insercao_ordenado = time.time() - start

    start = time.time()
    vetor_ordenado.pesquisa(valor_procurado)
    tempo_busca_ordenado = time.time() - start

    start = time.time()
    vetor_ordenado.pesquisa_binaria(valor_procurado)
    tempo_busca_binaria = time.time() - start

    start = time.time()
    vetor_ordenado.excluir(valor_procurado)
    tempo_exclusao_ordenado = time.time() - start

    # Vetor Não Ordenado
    vetor_nao_ordenado = VetorNaoOrdenado(tamanho)
    start = time.time()
    for valor in lista_aleatoria:
        vetor_nao_ordenado.insere(valor)
    tempo_insercao_nao_ordenado = time.time() - start

    start = time.time()
    vetor_nao_ordenado.pesquisa(valor_procurado)
    tempo_busca_nao_ordenado = time.time() - start

    start = time.time()
    vetor_nao_ordenado.excluir(valor_procurado)
    tempo_exclusao_nao_ordenado = time.time() - start

    # Exibir resultados
    print("\nVetor Ordenado:")
    print(f"Inserção: {tempo_insercao_ordenado:.6f}s")
    print(f"Busca Sequencial: {tempo_busca_ordenado:.6f}s")
    print(f"Busca Binária: {tempo_busca_binaria:.6f}s")
    print(f"Exclusão: {tempo_exclusao_ordenado:.6f}s")

    print("\nVetor Não Ordenado:")
    print(f"Inserção: {tempo_insercao_nao_ordenado:.6f}s")
    print(f"Busca Sequencial: {tempo_busca_nao_ordenado:.6f}s")
    print(f"Exclusão: {tempo_exclusao_nao_ordenado:.6f}s")


# Testar para tamanhos variados
comparar_operacoes(1000, random.randint(1, 10000))
comparar_operacoes(5000, random.randint(1, 10000))
comparar_operacoes(10000, random.randint(1, 10000))
