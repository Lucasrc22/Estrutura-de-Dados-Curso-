class No:
    def __init__(self):
        self.fila = []

    def mostrar_no(self):
        for elemento in self.fila:
            print(elemento, end=" ")
        print()  

    def enqueue(self, element):
        self.fila.append(element)

    def is_empty(self):
        return len(self.fila) == 0 

    def dequeue(self, index=0):  
        if not self.is_empty():
            if 0 <= index < len(self.fila):  
                return self.fila.pop(index)
            else:
                print("Índice inválido")
                return None
        else:
            print("A fila está vazia")
            return None

    def front(self):
        if not self.is_empty():
            self.mostrar_no()
        else:
            print("Fila está vazia")

    def size(self):
        return len(self.fila)  


fila = No()
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
fila.enqueue(6)
fila.enqueue(7)

fila.front()  

fila.dequeue(6)  
fila.front()  
