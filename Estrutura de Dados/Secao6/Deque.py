import numpy as np

class Deque:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.inicio = -1
        self.final = 0
        self.valores = np.empty(self.capacidade, dtype=int)

    def __deque_cheio(self):
        return (self.inicio == 0 and self.final == self.capacidade - 1) or (self.inicio == self.final + 1)

    def __deque_vazio(self):
        return self.inicio == -1

    def insere_inicio(self, valor):
        if self.__deque_cheio():
            print("Deque está cheio")
            return
        
        if self.inicio == -1:  # Deque vazio
            self.inicio = 0
            self.final = 0
        elif self.inicio == 0:  # Movimento circular para o início
            self.inicio = self.capacidade - 1
        else:
            self.inicio -= 1

        self.valores[self.inicio] = valor

    def insere_final(self, valor):
        if self.__deque_cheio():
            print("Deque está cheio")
            return

        if self.inicio == -1:  # Deque vazio
            self.inicio = 0
            self.final = 0
        elif self.final == self.capacidade - 1:  # Movimento circular para o final
            self.final = 0
        else:
            self.final += 1

        self.valores[self.final] = valor

    def excluir_inicio(self):
        if self.__deque_vazio():
            print("Deque está vazio")
            return

        self.valores[self.inicio] = 0  # Limpa o valor do início

        if self.inicio == self.final:  # Apenas um elemento
            self.inicio = -1
            self.final = -1
        elif self.inicio == self.capacidade - 1:  # Movimento circular
            self.inicio = 0
        else:
            self.inicio += 1

    def excluir_final(self):
        if self.__deque_vazio():
            print("Deque está vazio")
            return

        self.valores[self.final] = 0  # Limpa o valor do final

        if self.inicio == self.final:  # Apenas um elemento
            self.inicio = -1
            self.final = -1
        elif self.final == 0:  # Movimento circular
            self.final = self.capacidade - 1
        else:
            self.final -= 1

    def get_inicio(self):
        if self.__deque_vazio():
            print("Deque está vazio")
            return None
        return self.valores[self.inicio]
    
    def get_final(self):
        if self.__deque_vazio():
            print("Deque está vazio")
            return None
        return self.valores[self.final]


# Testando o Deque
deque = Deque(5)

print("Inserindo no final:")
deque.insere_final(10)
deque.insere_final(20)
deque.insere_final(30)
print("Valores após inserções no final:", deque.valores)

print("\nInserindo no início:")
deque.insere_inicio(5)
deque.insere_inicio(1)
print("Valores após inserções no início:", deque.valores)

print("\nTentando inserir no final em deque cheio:")
deque.insere_final(40)

print("\nExcluindo do início:")
deque.excluir_inicio()
print("Valores após excluir do início:", deque.valores)

print("\nExcluindo do final:")
deque.excluir_final()
print("Valores após excluir do final:", deque.valores)

print("\nPrimeiro elemento:", deque.get_inicio())
print("Último elemento:", deque.get_final())
