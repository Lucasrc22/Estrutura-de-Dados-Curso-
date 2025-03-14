class Node:
    def __init__(self, head):
        self.head = head
        self.next = None
    
    def show_node(self):
        print(self.head, end="->")
    
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
            print(current.head, end="->" if current.next else "")
            current = current.next
        print("\n")
    
    def delete_alternate(self):
        if self.head is None:
            return
        
        self.head = self.head.next  
        
        current = self.head
        while current is not None and current.next is not None:
            current.next = current.next.next  
            current = current.next

teste = ListaEncadeada()
teste.insert(8)
teste.insert(6)
teste.insert(1)
teste.insert(3)
teste.insert(5)
teste.insert(2)

teste.showNumber()
teste.delete_alternate()
teste.showNumber()
