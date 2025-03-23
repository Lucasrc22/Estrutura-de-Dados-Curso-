class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
    def showNode(self):
        print(self.value)

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
    def empty_list(self):
        return self.head is None
    
    def insere_head(self, value):
        new = Node(value)
        if self.empty_list():
            self.head = self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
    
    def insere_tail(self, value):
        new = Node(value)
        if self.empty_list():
            self.head = self.tail = new
        
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
    
    def exclude_head(self):
        if self.empty_list():
            print("The list is empty")
            return None
        
        temp = self.head
        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return temp.value
    
    def insere_tail(self, value):

        new = Node(value)
        if self.empty_list():
            self.head = self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            
    def exclude_tail(self):
        if self.empty_list():
            print("List is empty")
            return None
        
        temp = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return temp.value
        
    def show_list(self):
        if self.empty_list():
            print("The list is empty")
            return None
        current = self.head
        while current is not None:
            print(current.value, end= " ")
            current = current.next
        print()

lista = Deque()
lista.insere_head(10)
lista.insere_tail(20)
lista.insere_head(5)
lista.insere_tail(30)
print("Lista Completa")
lista.show_list()


lista.exclude_head()
print("Lista sem a extremidade superior")
lista.show_list()

lista.exclude_tail()
print("Lista sem a extremidade inferior")

lista.show_list()
print("Implementando nova head e tail")
lista.insere_head(9)
lista.insere_tail(40)
lista.show_list()
"""
Escolha da Estrutura: Lista Duplamente Encadeada

A estrutura escolhida para implementar o Deque foi a **Lista Duplamente Encadeada**, pois 
permite inserções e remoções eficientes tanto no início quanto no final da fila.  
Cada nó contém um ponteiro para o próximo elemento (`next`) e um para o anterior (`prev`), 
o que facilita operações nos dois extremos sem a necessidade de percorrer toda a estrutura.

📌 **Vantagens dessa abordagem**:
- **Eficiência**: Inserções e remoções nos extremos ocorrem em O(1), sem deslocamento de elementos.
- **Flexibilidade**: Cresce e encolhe dinamicamente sem necessidade de alocação fixa de memória.
- **Acesso direto ao último elemento**: Diferente da lista simplesmente encadeada, podemos remover 
  o último elemento diretamente sem percorrer toda a lista.

Essa abordagem é ideal para situações onde há a necessidade frequente de adicionar e remover 
elementos tanto no início quanto no final da fila, como em filas de atendimento e buffers de comunicação.

"""