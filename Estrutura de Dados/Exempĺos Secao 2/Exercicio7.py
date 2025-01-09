#Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros e os armazene dentro de uma lista. 
#Após a leitura, crie outra estrutura de repetição para somar todos os valores digitados
import numpy as np

lista = []
for i in range(1,6):
    num = int(input(f'Digite o numero {i}: '))
    lista.append(num)
    i+=1
print('Lista: ',lista)

soma = 0
for numero in range(len(lista)):
    soma += lista[numero]
print('Soma dos valores: ', soma)


print('soma em np array: ',np.array(lista).sum())