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

        dummy = Node(0)  
        current = dummy  

        list1 = self.head  
        list2 = another_list.head  
        while list1 and list2:
            if list1.data < list2.data:  
                current.next = list1
                list1 = list1.next
            else:  
                current.next = list2
                list2 = list2.next
            current = current.next  

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        self.head = dummy.next



list1 = ListaEncadeada()

list1 = ListaEncadeada()
list1.inserir(8)
list1.inserir(7)
list1.inserir(6)
list1.inserir(5)

list2 = ListaEncadeada()
list2.inserir(4)
list2.inserir(3)
list2.inserir(2)
list2.inserir(1)


print("Lista 1:")
list1.exibir()
print("Lista 2:")
list2.exibir()


list1.mesclar_listas_ordenadas(list2)

print("\nLista combinada ordenada:")
list1.exibir()
