#Matriz: Dada a matriz abaixo, construa uma estrutura de 
#repetição para percorrer e somar todos os elementos da matriz

import numpy as np

matriz = np.array([[3, 4, 1], [3, 1, 5]])
print(matriz.shape)
def somaMatriz(matriz):
    soma = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
    print("A soma de todos os elementos da matriz é:", soma)


somaMatriz(matriz)

print()
soma = 0
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma += matriz[i][j]

print('soma metodo professor: ', soma)
