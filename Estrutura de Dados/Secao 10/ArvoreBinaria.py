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

    def inserir(self, valor):
        novo = No(valor)

        #se a arvore estiver vazia

        if self.raiz == None:
            self.raiz = novo
        else:
            atual = self.raiz
            while True:
                pai = atual
                #esquerdaa
                if valor < atual.valor:
                    atual= atual.esquerda
                    if atual == None:
                        pai.esquerda = novo
                        return
                #direita
                else:
                    atual = atual.direita
                    if atual == None:
                        pai.direita = novo
                        return

arvore = ArvoreBuscaBinaria()
arvore.inserir(53)
arvore.inserir(54)
arvore.inserir(23)
arvore.inserir(87)
arvore.inserir(98)
arvore.inserir(22)
arvore.inserir(12)
arvore.inserir(11)
arvore.inserir(10)

print(arvore.raiz.esquerda.valor)
