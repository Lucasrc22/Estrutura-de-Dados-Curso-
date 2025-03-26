class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None

class ListaEncadeada:
    def __init__(self):
        self.head = None

    def insert_in_order(self, name, age):
        new_person = Person(name, age)

        if self.head is None or self.head.age > age:
            new_person.next = self.head
            self.head = new_person
            return

        current = self.head
        while current.next and current.next.age < age:
            current = current.next

        new_person.next = current.next
        current.next = new_person

    def show_list(self):
        current = self.head
        while current:
            print(f"{current.name} ({current.age})", end=" ")
            current = current.next
    
def merge_sorted_lists(list1, list2):
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1


    if list1.head.age < list2.head.age:
        merged_head = list1.head
        list1.head = list1.head.next
    else:
        merged_head = list2.head
        list2.head = list2.head.next

    merged_current = merged_head

   
    while list1.head and list2.head:
        if list1.head.age < list2.head.age:
            merged_current.next = list1.head
            list1.head = list1.head.next
        else:
            merged_current.next = list2.head
            list2.head = list2.head.next
        merged_current = merged_current.next


    merged_current.next = list1.head if list1.head else list2.head

    merged_list = ListaEncadeada()
    merged_list.head = merged_head
    return merged_list

list1 = ListaEncadeada()
list1.insert_in_order("Lucas", 25)
list1.insert_in_order("Maria", 21)
list1.insert_in_order("Guilherme", 20)

list2 = ListaEncadeada()
list2.insert_in_order("Zuila", 52)
list2.insert_in_order("Duda", 24)

# Exibindo as listas antes da mesclagem
print("Lista 1:")
list1.show_list()
print()
print("Lista 2:")
list2.show_list()

# Mesclando as listas ordenadas
merged_list = merge_sorted_lists(list1, list2)

# Exibindo a lista final
print()
print("Lista Mesclada:")
merged_list.show_list()
print()

"""

Eficiência:
O algoritmo percorre cada lista apenas uma vez, realizando comparações e atribuições.
Como cada nó é visitado no máximo uma vez, a complexidade do algoritmo é O(n), onde n é o número total de nós nas duas listas.
Essa complexidade é ótima para esse tipo de problema, pois não requer passes adicionais.

Possíveis otimizações:
Uso de ponteiros em vez de modificar os nós das listas:
Atualmente, modificamos os ponteiros da lista original, o que pode dificultar a reutilização.
Uma alternativa seria criar uma nova lista e copiar os nós, preservando as listas originais.

Implementação iterativa mais enxuta:
Utilizar um nó `dummy` para evitar verificações adicionais ao definir o primeiro nó da lista mesclada.
Isso evitaria a necessidade do bloco de código separado para definir `merged_head`.

"""