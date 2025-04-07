class Pilha:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def show(self):
        print(self.items)

def inverter_pilha(pilha):
    pilha_aux = Pilha()

    while not pilha.is_empty():
        pilha_aux.push(pilha.pop())

    return pilha_aux


p = Pilha()
p.push(1)
p.push(2)
p.push(3)
p.push(4)

print("Pilha original:")
p.show()

p_invertida = inverter_pilha(p)

print("Pilha invertida:")
p_invertida.show()
