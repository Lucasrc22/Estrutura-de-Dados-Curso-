from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class PilhaDeque:
    def __init__(self):
        self.items = deque()
    
    def push(self, value):
        self.items.append(value)
    
    def pop(self):
        if self.items:
            return self.items.pop()
    
    def show(self):
        print(list(self.items))


class PilhaEncadeada:
    def __init__(self):
        self.topo = None
    
    def push(self, value):
        novo = Node(value)
        novo.next = self.topo
        self.topo = novo
    
    def pop(self):
        if self.topo:
            valor = self.topo.value
            self.topo = self.topo.next
            return valor
    
    def show(self):
        atual = self.topo
        pilha = []
        while atual:
            pilha.append(atual.value)
            atual = atual.next
        print(pilha)


print("Testando Pilha com deque")
p1 = PilhaDeque()
p1.push(10)
p1.push(20)
p1.push(30)
p1.show()
p1.pop()
p1.show()

print("\n Testando Pilha com Lista Encadeada")
p2 = PilhaEncadeada()
p2.push(10)
p2.push(20)
p2.push(30)
p2.show()
p2.pop()
p2.show()
