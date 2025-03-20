class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserir(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_lista(self):
        current = self.head
        while current:
            print(current.value, end="   ")
            current = current.next
        print("")

    def remover_duplicatas(self):
        if not self.head:
            return
        
        saw_values = set()
        current = self.head
        saw_values.add(current.value)

        while current.next:
            if current.next.value in saw_values:
                current.next = current.next.next 
            else:
                saw_values.add(current.next.value)
                current = current.next

lista = ListaEncadeada()
lista.inserir(3)
lista.inserir(1)
lista.inserir(4)
lista.inserir(3)
lista.inserir(1)
lista.inserir(6)
lista.inserir(1)

lista.inserir(4)

lista.inserir(7)



print("Lista original:")
lista.print_lista()

lista.remover_duplicatas()

print("Lista após remover duplicatas:")
lista.print_lista()
