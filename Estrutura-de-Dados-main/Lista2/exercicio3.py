class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueue:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.size = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == self.capacidade:
            self.dequeue()

        if not self.head:
            self.head = self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def dequeue(self):
        if not self.head:
            return None
        
        removed_value = self.head.value

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

        self.size -= 1
        return removed_value

    def show(self):
        if not self.head:
            print("Fila vazia")
            return

        atual = self.head
        for _ in range(self.size):
            print(atual.value, end=" ")
            atual = atual.next
        print("")


fila = CircularQueue(5)
fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)
fila.enqueue(40)
fila.enqueue(50)
fila.show()
fila.enqueue(60)
fila.show()
fila.enqueue(70)
fila.show()
fila.enqueue(80)
fila.show()
fila.enqueue(90)
fila.show()
