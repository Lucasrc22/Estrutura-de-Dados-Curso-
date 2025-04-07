class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Fila:
    def __init__(self):
        self.head = None
        self.tail = None

    def esta_vazia(self):
        return self.head is None

    def enqueue(self, value):
        novo_no = Node(value)
        if self.esta_vazia():
            self.head = self.tail = novo_no
        else:
            self.tail.next = novo_no
            self.tail = novo_no

    def dequeue(self):
        if self.esta_vazia():
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp.value

    def mostrar(self):
        atual = self.head
        while atual:
            print(atual.value, end=" ")
            atual = atual.next
        print()

def remover_duplicatas(fila):
    if fila.esta_vazia():
        return

    vistos = set()
    nova_fila = Fila()

    atual = fila.head
    while atual:
        if atual.value not in vistos:
            vistos.add(atual.value)
            nova_fila.enqueue(atual.value)
        atual = atual.next

    fila.head = nova_fila.head
    fila.tail = nova_fila.tail

fila = Fila()
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(10)
fila.enqueue(30)
fila.enqueue(20)
fila.enqueue(40)
fila.enqueue(50)
fila.enqueue(50)
fila.enqueue(60)

print("fila original:")
fila.mostrar()

remover_duplicatas(fila)

print("fila sem duplicatas:")
fila.mostrar()
