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
        new_node = Node(value)

        if self.empty_list():
            self.head = self.tail = new_node
        
        else:
            new_node.next = self.head

            self.head = new_node
    
    def insere_tail(self, value):
        new_node = Node(value)
    
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
            current = current.next

        temp = self.tail
        current.next = None
        self.tail = current
        return temp.value
        
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print("")
        
d = Deque()

d.insere_head(10)
d.insere_tail(20)
d.insere_head(5)
d.insere_tail(30)
d.insere_head(1)
d.insere_tail(40)
d.insere_head(0)
d.insere_tail(50)

print("Lista após várias inserções (head/tail alternadas):")
d.show()

d.exclude_head()
d.exclude_tail()

print("Após remover uma da head e uma da tail:")
d.show()

d.insere_head(100)
d.insere_tail(200)
d.insere_tail(300)
d.insere_head(-10)

print("Após novas inserções:")
d.show()

d.exclude_tail()
d.exclude_tail()
d.exclude_tail()
d.exclude_head()
d.exclude_head()
d.exclude_head()

print("Após esvaziar completamente:")
d.show()


""" Vantagens

- Simplicidade, a implementação eh mais enxuta, pois cada nó possui apenas
um ponteiro, nextm reduzindo o uso de memória

    Limitações

-Remover do final é ineficiente, pois tem que percorrer a lista inteira
para encontrar o penultimo nó. Ou seja, para funções de fim da fila
ela não recomendada.

"""