import numpy as np

class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.visitado = False
        self.distancia_objetivo = distancia_objetivo
        self.adjacentes = []

    def adiciona_adjacente(self, adjacente):
        self.adjacentes.append(adjacente)

    def mostra_adjacentes(self):
        for i in self.adjacentes:
            print(i.vertice.rotulo, i.custo)

class Adjacente:
    def __init__(self, vertice, custo):
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objetivo + self.custo

class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def insere(self, adjacente):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela:
                break
            if i == self.ultima_posicao:
                posicao = i + 1
        x = self.ultima_posicao
        while x >= posicao:
            self.valores[x + 1] = self.valores[x]
            x -= 1
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i].vertice.rotulo, ' - ',
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objetivo, ' - ',
                      self.valores[i].distancia_aestrela)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"{i} - {self.valores[i].vertice.rotulo} - {self.valores[i].custo} - {self.valores[i].vertice.distancia_objetivo} - {self.valores[i].distancia_aestrela}")

    def excluir(self, rotulo):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] is not None and self.valores[i].vertice.rotulo == rotulo:
                for j in range(i, self.ultima_posicao):
                    self.valores[j] = self.valores[j + 1]
                self.valores[self.ultima_posicao] = None
                self.ultima_posicao -= 1
                return
        print("Elemento não encontrado.")

# Testes
vetor = VetorOrdenado(10)

vetor.insere(Adjacente(Vertice("A", 3), 1))
vetor.insere(Adjacente(Vertice("B", 4), 2))
vetor.insere(Adjacente(Vertice("C", 6), 3))

vetor.imprime()
print()

vetor.insere(Adjacente(Vertice("D", 5), 2))
vetor.imprime()

vetor.excluir("B")
vetor.imprime()
