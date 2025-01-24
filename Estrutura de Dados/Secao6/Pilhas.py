

import numpy as np

class Pilha:
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=object)  # Permite armazenar objetos genéricos

    def __pilhaCheia(self):
        return self.__topo == self.__capacidade - 1
    
    def __pilhaVazia(self):
        return self.__topo == -1
    
    def empilhar(self, valor):
        if self.__pilhaCheia():
            print("A Pilha está cheia")
        else:
            self.__topo += 1
            self.__valores[self.__topo] = valor  # Armazena qualquer objeto
    
    def desempilhar(self):
        if self.__pilhaVazia():
            print("A Pilha está vazia")
            return None  # Retorna None se a pilha estiver vazia
        else:
            valor_removido = self.__valores[self.__topo]
            self.__valores[self.__topo] = None  # Limpa o espaço na pilha
            self.__topo -= 1
            return valor_removido  # Retorna o objeto removido
    
    def verTopo(self):
        if self.__pilhaVazia():
            print("A Pilha está vazia")
            return None
        else:
            return self.__valores[self.__topo]  # Retorna o objeto no topo da pilha


# Execução com exemplo

# Criando uma pilha com capacidade para 5 elementos
minha_pilha = Pilha(5)

# Empilhando elementos
minha_pilha.empilhar(10)
minha_pilha.empilhar(20)
minha_pilha.empilhar(30)
print("Topo após empilhar 3 elementos:", minha_pilha.verTopo())  # Saída: 30

# Desempilhando um elemento
removido = minha_pilha.desempilhar()
print("Elemento desempilhado:", removido)  # Saída: 30
print("Topo atual após desempilhar:", minha_pilha.verTopo())  # Saída: 20

# Continuando operações
minha_pilha.empilhar(40)
minha_pilha.empilhar(50)
minha_pilha.empilhar(60)  # Tentativa de empilhar com a pilha cheia
print("Topo após empilhar mais elementos:", minha_pilha.verTopo())  # Saída: 50

# Desempilhando todos os elementos
while True:
    removido = minha_pilha.desempilhar()
    if removido is None:  # Pilha vazia
        break
    print("Elemento desempilhado:", removido)

print("Tentando desempilhar novamente:")
minha_pilha.desempilhar()  # Pilha está vazia
