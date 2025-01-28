import numpy as np

class FilaCircular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = 0
        self.final = -1
        self.numerosElementos = 0
        self.valores = np.empty(self.capacidade, dtype=object)

    def fila_vazia(self):  # Método público agora
        return self.numerosElementos == 0

    def __fila_cheia(self):
        return self.numerosElementos == self.capacidade

    def enfileirar(self, valor):
        if self.__fila_cheia():
            print("A fila está cheia")
            return
        
        # Incremento circular para o final
        self.final = (self.final + 1) % self.capacidade
        self.valores[self.final] = valor
        self.numerosElementos += 1

    def desenfileirar(self):
        if self.fila_vazia():
            print("A fila já está vazia")
            return None
        
        temp = self.valores[self.inicio]
        
        # Incremento circular para o início
        self.inicio = (self.inicio + 1) % self.capacidade
        self.numerosElementos -= 1
        return temp

    def primeiro(self):
        if self.fila_vazia():
            return -1
        return self.valores[self.inicio]


# Exemplo de uso
fila = FilaCircular(5)

# Enfileirar elementos
fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.enfileirar(40)
fila.enfileirar(50)

print("Tentando enfileirar com a fila cheia:")
fila.enfileirar(60)  # Deve mostrar que a fila está cheia

# Desenfileirar elementos
print("\nDesenfileirando elementos:")
print(fila.desenfileirar())  # Deve remover 10
print(fila.desenfileirar())  # Deve remover 20

# Enfileirar mais elementos
fila.enfileirar(60)
fila.enfileirar(70)

# Ver o primeiro elemento
print("\nPrimeiro elemento da fila:", fila.primeiro())  # Deve mostrar 30

# Desenfileirando todos os elementos
print("\nDesenfileirando todos os elementos:")
while not fila.fila_vazia():  # Método agora é público e chamável diretamente
    print(fila.desenfileirar())
