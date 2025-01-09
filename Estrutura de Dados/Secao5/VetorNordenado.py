import numpy as np

class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultimaPosicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)

    # O(n)
    def imprimir(self):
        if self.ultimaPosicao == -1:
            print("O vetor está vazio")
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, " - ", self.valores[i])

    # O(1)
    def inserir(self, valor):
        if self.ultimaPosicao == self.capacidade - 1:
            print("Capacidade máxima atingida")
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor

    # O(n)
    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao + 1):
            if valor == self.valores[i]:
                return i
        return -1  # Fora do loop

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao -= 1

# Teste
vetor = VetorNaoOrdenado(5)

vetor.inserir(3)
vetor.inserir(5)
vetor.inserir(8)
vetor.inserir(1)
vetor.inserir(7)

print("Antes da exclusão:")
vetor.imprimir()

print("\nExcluindo o valor 5...")
vetor.excluir(7)

print("\nDepois da exclusão:")
vetor.imprimir()
