#antes: 8-> 6-> 1-> 3-> 5-> 2
#depois: 6-> 3-> 2


class Node:
    def __init__(self, head):
        self.head= head
        self.next = None
    
    def show_node(self):
        print(self.head, end ="->")
    
class ListaEncadeada:
    def __init__(self):
        self.head = None

    def insert(self, head):
        new = Node(head)
        if self.head is None:
            self.head = new
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new
    def showNumber(self):
        current = self.head
        while current is not None:
            current.show_node()
            current = current.next
        print("End")

    def delete_alternate(self):
        # Esse método percorre a lista e alterna a exclusão de nós
        current = self.head
        count = 0
        
        # Enquanto houver mais de um nó na lista
        while current is not None and current.next is not None:
            if count % 2 == 0:  # Nos índices 0, 2, 4... (a contagem começa em 0)
                current = current.next  # Mantém o nó atual
            else:
                # Exclui o próximo nó
                next_node = current.next
                current.next = next_node.next  # Remove o nó seguinte
            count += 1
        
        # No final, é importante manter o último nó da lista
        if count % 2 == 0 and current is not None:
            current.next = None


teste = ListaEncadeada()
teste.insert(8)

teste.insert(6)

teste.insert(1)

teste.insert(3)

teste.insert(5)

teste.insert(2)

teste.showNumber()
print()
teste.delete_alternate()
teste.showNumber()