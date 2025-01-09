import numpy as np

class FilaPrioridade:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numerosElementos = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __fila_vazia(self):  
        return self.numerosElementos == 0

    def __fila_cheia(self):
        return self.numerosElementos == self.capacidade
    
    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("Fila está cheia")
            return
        
        if self.numerosElementos ==0:
            self.valores[self.numerosElementos] = valor
            self.numerosElementos += 1
        else:
            x =self.numerosElementos -1
            while x>= 0:
                if valor > self.valores[x]:
                    self.valores[x + 1] = self.valores[x]
                else:
                    break
                    
                x-=1
            self.valores[x+1] = valor
            self.numerosElementos +=1

    def desinfileirar(self):
        if self.__fila_vazia():
            print("Sua Fila está vazia")
            return
        valor = self.valores[self.numerosElementos - 1]
        self.numerosElementos -=1
        return valor


    def primeiro(self):
        if self.__fila_vazia():
            return -1
        else:
            return self.valores[self.numerosElementos -1]

print()
# Testes com a FilaPrioridade

fila = FilaPrioridade(5)

print("Primeiro elemento na fila (esperado: -1, pois está vazia):", fila.primeiro())

# Enfileirando elementos
fila.enfileirar(30)
fila.enfileirar(50)
fila.enfileirar(10)

print("\nApós adicionar 30, 50, e 10:")
print("Primeiro elemento (maior valor):", fila.primeiro())  # Esperado: 50

fila.enfileirar(40)
fila.enfileirar(20)

print("\nApós adicionar 40 e 20:")
print("Primeiro elemento (maior valor):", fila.primeiro())  # Esperado: 50

# Tentando enfileirar na fila cheia
fila.enfileirar(60)  # Esperado: Mensagem de fila cheia

# Desenfileirando elementos
print("\nDesenfileirando elementos:")
print(fila.desinfileirar())  # Esperado: 50 (maior prioridade)
print(fila.desinfileirar())  # Esperado: 40
print(fila.desinfileirar())  # Esperado: 30

print("\nPrimeiro elemento após algumas remoções (esperado: 20):", fila.primeiro())

fila.desinfileirar()  # Remove 20
fila.desinfileirar()  # Remove 10

# Tentando desenfileirar de uma fila vazia
print("\nTentando desenfileirar de uma fila vazia:")
fila.desinfileirar()

print("\nPrimeiro elemento em uma fila vazia (esperado: -1):", fila.primeiro())
