class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

def altura(no):
    return no.altura if no else 0

def fator_balanceamento(no):
    return altura(no.esquerda) - altura(no.direita) if no else 0

def rotacao_direita(y):
    x = y.esquerda
    T2 = x.direita
    x.direita = y
    y.esquerda = T2
    y.altura = 1 + max(altura(y.esquerda), altura(y.direita))
    x.altura = 1 + max(altura(x.esquerda), altura(x.direita))
    return x

def rotacao_esquerda(x):
    y = x.direita
    T2 = y.esquerda
    y.esquerda = x
    x.direita = T2
    x.altura = 1 + max(altura(x.esquerda), altura(x.direita))
    y.altura = 1 + max(altura(y.esquerda), altura(y.direita))
    return y

def rotacao_dupla_direita(z):
    z.esquerda = rotacao_esquerda(z.esquerda)
    return rotacao_direita(z)

def rotacao_dupla_esquerda(z):
    z.direita = rotacao_direita(z.direita)
    return rotacao_esquerda(z)

def inserir(no, valor):
    if no is None:
        return Node(valor)
    if valor < no.valor:
        no.esquerda = inserir(no.esquerda, valor)
    elif valor > no.valor:
        no.direita = inserir(no.direita, valor)
    else:
        return no
    no.altura = 1 + max(altura(no.esquerda), altura(no.direita))
    fb = fator_balanceamento(no)
    if fb > 1 and valor < no.esquerda.valor:
        return rotacao_direita(no)
    if fb < -1 and valor > no.direita.valor:
        return rotacao_esquerda(no)
    if fb > 1 and valor > no.esquerda.valor:
        return rotacao_dupla_direita(no)
    if fb < -1 and valor < no.direita.valor:
        return rotacao_dupla_esquerda(no)
    return no

def em_ordem(no):
    if no is None:
        return []
    return em_ordem(no.esquerda) + [no.valor] + em_ordem(no.direita)

if __name__ == "__main__":
    raiz = None
    valores = [30, 10, 20,50,70,15,12,56]
    for v in valores:
        raiz = inserir(raiz, v)
    print(em_ordem(raiz))
