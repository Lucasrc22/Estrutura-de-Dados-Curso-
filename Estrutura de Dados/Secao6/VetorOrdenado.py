import numpy as np


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(N)
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
            if self.valores[i] > valor:
                return -1
            if self.valores[i] == valor:
                return i
        return -1

    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultimaPosicao
        passos = 0
        while limite_inferior <= limite_superior:
            passos += 1
            posicao_atual = int((limite_inferior + limite_superior))// 2

            if self.valores[posicao_atual] == valor:
                print(f"Valor encontrado após {passos} passos.")
                return posicao_atual
            elif self.valores[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
            else:
                limite_superior = posicao_atual - 1
        print(f"Valor não encontrado após {passos} passos.")
        return -1  # Elemento não encontrado

    def excluir(self, valor):
        posicao = self.pesquisa(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao -= 1
    

# Testes
vetor = VetorOrdenado(10)

vetor.insere(3)
vetor.insere(4)
vetor.insere(6)

vetor.imprime()
print()
vetor.insere(5)
vetor.imprime()
print(vetor.pesquisa(5))
print(vetor.pesquisa(2))
vetor.excluir(4)
vetor.imprime()
print()

vetor = VetorOrdenado(101)

for i in range(1, 101):
    vetor.insere(i)

vetor.imprime()

# Testes de pesquisa binária
print(vetor.pesquisa_binaria(100))
