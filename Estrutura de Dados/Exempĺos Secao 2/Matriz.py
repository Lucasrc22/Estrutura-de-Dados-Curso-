import numpy as np

matriz = np.array([[2,3,4],[4,5,7]])

print(matriz)

print()

print(matriz.shape)

print(matriz[0])

print(matriz[0][2])
print()
for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        print(matriz[i][j])