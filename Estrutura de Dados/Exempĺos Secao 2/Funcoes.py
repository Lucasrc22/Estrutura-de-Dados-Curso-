#funcao sem parametro e sem retorno

def mensagem():
    print('texto da funcao')

mensagem()

#funcao com passagem de parametro

def mensagem(texto):
    print(texto)
mensagem("texto com parametro")

def soma(a, b):
    print(a+b)
soma(2,3)

#funcao com passagem de parametro e retorno
def soma(a,b):
    return a+b

r = soma(5,5)
print(r)

def calculaEnergiaPotencialGravitacional(m,h, g =10):
    e = g*m*h
    return print(e)

calculaEnergiaPotencialGravitacional(30,12,9.8)