import numpy as np


class Vertice:
    def __init__(self, rotulo, distancia_objetivo):
        self.rotulo = rotulo
        self.distancia_objetivo = distancia_objetivo

    def __repr__(self):
        return f"{self.rotulo} ({self.distancia_objetivo})"


class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=object)

    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"{i} - {self.valores[i].rotulo} - {self.valores[i].distancia_objetivo}")

    def insere(self, vertice):
        if self.ultima_posicao >= self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] is not None and self.valores[i].distancia_objetivo > vertice.distancia_objetivo:
                break
            posicao = i + 1  # Atualiza a posição correta
        
        # Deslocamento dos elementos para abrir espaço
        for j in range(self.ultima_posicao, posicao - 1, -1):
            self.valores[j + 1] = self.valores[j]

        # Insere o novo vértice na posição correta
        self.valores[posicao] = vertice
        self.ultima_posicao += 1

    def pesquisa(self, rotulo):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] is not None and self.valores[i].rotulo == rotulo:
                return i
        return -1

    def pesquisa_binaria(self, rotulo):
        limite_inferior = 0
        limite_superior = self.ultima_posicao
        passos = 0

        while limite_inferior <= limite_superior:
            passos += 1
            posicao_atual = (limite_inferior + limite_superior) // 2

            if self.valores[posicao_atual] is not None and self.valores[posicao_atual].rotulo == rotulo:
                print(f"Valor encontrado após {passos} passos.")
                return posicao_atual
            elif self.valores[posicao_atual] is None or self.valores[posicao_atual].rotulo < rotulo:
                limite_inferior = posicao_atual + 1
            else:
                limite_superior = posicao_atual - 1

        print(f"Valor não encontrado após {passos} passos.")
        return -1

    def excluir(self, rotulo):
        posicao = self.pesquisa(rotulo)
        if posicao == -1:
            print("Elemento não encontrado.")
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.valores[self.ultima_posicao] = None  # Remove a referência ao último item
            self.ultima_posicao -= 1


# Testes
vetor = VetorOrdenado(10)

vetor.insere(Vertice("A", 3))
vetor.insere(Vertice("B", 4))
vetor.insere(Vertice("C", 6))

vetor.imprime()
print()

vetor.insere(Vertice("D", 5))
vetor.imprime()
print(vetor.pesquisa("D"))  # Deve retornar a posição do vértice "D"
print(vetor.pesquisa("X"))  # Deve retornar -1

vetor.excluir("B")
vetor.imprime()
print()

# Teste com maior quantidade de elementos
vetor = VetorOrdenado(101)

for i in range(1, 101):
    vetor.insere(Vertice(str(i), i))

vetor.imprime()

# Teste de pesquisa binária
print(vetor.pesquisa_binaria("100"))
print(vetor.pesquisa_binaria("50"))
print(vetor.pesquisa_binaria("200"))  # Deve retornar -1
