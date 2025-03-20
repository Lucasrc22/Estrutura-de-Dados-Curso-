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
        new = Node(head) #Cria um novo Nó
        if self.head is None: # Se a lista estiver vazia, crie o primeiro nó
            self.head = new
        else:
            current = self.head #começa pelo primeiro nó
            while current.next is not None: #percorre até o último nó 
                current = current.next
            current.next = new #insere o novo nó no final
    
    def showNumber(self):
        current = self.head
        while current is not None:
            print(current.head, end="->" if current.next else "")
            current = current.next
        print("\n")
    
    def delete_alternate(self):
        if self.head is None:
            return #Se a lista estiver vazia, não faz nada
        
        self.head = self.head.next #remove o primeiro nó
        
        current = self.head
        while current is not None and current.next is not None:
            current.next = current.next.next #Remove o próximo do próximo nó 
            current = current.next #avança para o próximo nó

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
