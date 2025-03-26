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
        """
        eficiente 
        porque a busca em um conjunto é feita em 
        tempo constante (O(1)).
        Cria um conjunto vazio chamado saw_values 
        que será usado para rastrear os valores que 
        já foram encontrados enquanto percorremos a lista
        """
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

"""
 Remove elementos duplicados mantendo a primeira ocorrência.

Complexidade de Tempo:
O(N), pois percorremos a lista apenas uma vez e usamos um conjunto (set)
para armazenar os valores já vistos, que tem operações O(1) em média.

Complexidade de Espaço:
O(N), pois utilizamos um conjunto adicional para armazenar os valores únicos.

Otimizações Possíveis:
Se a lista estiver ordenada, podemos remover duplicatas sem usar `set`,
apenas comparando elementos consecutivos, reduzindo a complexidade espacial para O(1).
Se não houver restrição de memória, um dicionário (`dict`) pode ser usado
para armazenar a frequência dos elementos e permitir estatísticas rápidas.
"""