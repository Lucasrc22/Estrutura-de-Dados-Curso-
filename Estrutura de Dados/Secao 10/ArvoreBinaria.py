class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
    
    def mostrar_no(self):
        print(self.valor)

class ArvoreBuscaBinaria:
    def __init__(self):
        self.raiz = None