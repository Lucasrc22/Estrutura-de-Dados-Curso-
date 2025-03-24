class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class ListaEncadeada:
    def __init__(self):
        self.head = None
    
    def inserir(self, data):
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node
        
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_Node
    
    def exibir(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print("")

    def mesclar_listas_ordenadas(self, another_list):
        """
        Função que recebe outra lista ordenada e mescla com a lista atual de forma ordenada
        Cria um nó cabeça falso para a nova lista combinada
        """

        # Análise da Complexidade:
        # Complexidade temporal: Como estamos percorrendo as duas listas uma vez, a complexidade é O(n + m), onde n e m são o número de elementos nas duas listas.
        #
        # Complexidade espacial: A complexidade espacial é O(1) extra, pois estamos apenas alterando os ponteiros existentes e não criando novas estruturas de dados (exceto para o nó "dummy").
        #
        # Otimizações:
        # - Evitar cópias desnecessárias: A função já evita criar novas listas, simplesmente ajustando os ponteiros, o que torna o algoritmo muito eficiente em termos de memória.
        # 
        # - Evitar verificações desnecessárias: A função usa o nó "dummy" para evitar verificações no início da lista, o que simplifica o código e pode ter um pequeno ganho de performance.
        
        dummy = Node(0)  # Nó cabeça falso
        current = dummy  # Ponteiro atual para percorrer a nova lista mesclada

        list1 = self.head  # Ponteiro para a primeira lista
        list2 = another_list.head  # Ponteiro para a segunda lista

        # Enquanto ambas as listas tiverem nós, comparamos os valores e vamos adicionando à nova lista
        while list1 and list2:
            if list1.data < list2.data:  # Se o valor da list1 for menor, adiciona o nó da list1
                current.next = list1
                list1 = list1.next
            else:  # Caso contrário, adiciona o nó da list2
                current.next = list2
                list2 = list2.next
            current = current.next  # Avança para o próximo nó

        # Se houver nós restantes em qualquer uma das listas, os adiciona à nova lista
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # Atualiza a cabeça da lista com o início da nova lista mesclada
        self.head = dummy.next


# Testando a função de mesclagem

# Lista 1: 1 -> 3 -> 5 -> 7
list1 = ListaEncadeada()
list1.inserir(1)
list1.inserir(3)
list1.inserir(5)
list1.inserir(7)

# Lista 2: 2 -> 4 -> 6 -> 8
list2 = ListaEncadeada()
list2.inserir(2)
list2.inserir(4)
list2.inserir(6)
list2.inserir(8)

# Exibindo as listas antes da mesclagem
print("Lista 1:")
list1.exibir()
print("Lista 2:")
list2.exibir()

# Mescla as duas listas ordenadas
list1.mesclar_listas_ordenadas(list2)

# Exibindo a lista combinada ordenada
print("\nLista combinada ordenada:")
list1.exibir()
