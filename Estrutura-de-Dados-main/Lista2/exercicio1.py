class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty_list(self):
        return self.head is None


    def insere_head(self,value):
        new_node = Node()

        if self.empty_list():
            self.head = self.tail = new_node
        
        else:
            new_node.next = self.head

            self.head = new_node
    
    def insere_tail(self, value):
        new_node = Node()
    
        if self.empty_list():
            self.head = self.tail = Node()
        
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def exclude_head(self):
        if self.empty_list():
            return None
        
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        
        return temp.value
    
    def exclude_tail(self):
        if self.empty_list():
            return None
        if self.head == self.tail:
            temp = self.tail
            self.head = self.tail = None
            return temp.value
        
        current = self.head
        while current.next != self.tail:
            temp = self.tail
            current.next = None
            self.tail = current
            return temp.value
        
""" Vantagens

- Simplicidade, a implementação eh mais enxuta, pois cada nó possui apenas
um ponteiro, nextm reduzindo o uso de memória

    Limitações

-Remover do final é ineficiente, pois tem que percorrer a lista inteira
para encontrar o penultimo nó

"""