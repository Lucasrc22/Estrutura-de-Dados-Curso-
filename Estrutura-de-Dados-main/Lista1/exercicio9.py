class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.next = None
    

class ListaEncadeadaCircular:
    def __init__(self):
        self.head = None

    
    def insert_in_order(self, name, age):
        newPerson = Person(name, age)

        if self.head is None:
            self.head = newPerson
            self.head.next = self.head
            return
        
        current = self.head

        if age < self.head.age:
            while current.next != self.head:
                current = current.next
            
            current.next = newPerson
            newPerson.next = self.head
            self.head = newPerson
            return
        
        while current.next != self.head and current.next.age < age:
            current = current.next
        
        newPerson.next = current.next
        current.next = newPerson
    
    def show_lista(self):
        if self.head is None:
            print("List is empty")
            return
        
        current = self.head

        while True:
            print(f"{current.name}  ({current.age})" )
            current = current.next
            if current == self.head:
                break

lista = ListaEncadeadaCircular()
lista.insert_in_order("Lucas", 24)
lista.insert_in_order("Zuila", 52)
lista.insert_in_order("Maria", 21)
lista.insert_in_order("Guilherme", 20)
lista.insert_in_order("Duda", 25)

lista.show_lista()