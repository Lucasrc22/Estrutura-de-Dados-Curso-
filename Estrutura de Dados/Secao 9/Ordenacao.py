import numpy as np
import random as random
import time as tm
def bubble_sort(vetor):
    n = len(vetor)

    for i in range(n):
        for j in range(0, n-i-1):
            if vetor[j] > vetor[j+1]:
                temp = vetor[j]
                vetor[j] = vetor[j +1]
                vetor[j + 1] = temp

    return vetor


def selection_sort(vetor):
    n = len(vetor)

    for i in range(n):
        id_minimo = i
        for j in range(i + 1, n):
            if vetor[id_minimo] > vetor[j]:
                id_minimo = j
            
        temp = vetor[i]
        vetor[i] = vetor[id_minimo]
        vetor[id_minimo] = temp
    return vetor

def insertion_sort(vetor):
    n = len(vetor)
    for i in  range(1, n):
        marcado = vetor[i]
        j = i -1
        while j >= 0 and marcado < vetor[j]:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j +1] = marcado

    return vetor
def shell_sort(vetor):
    intervalo = len(vetor) //2

    while intervalo > 0:
        for i in range(intervalo, len(vetor)):
            temp = vetor[i]
            j = i
            while j >= intervalo and vetor[j - intervalo] > temp:
                vetor[j] = vetor[j - intervalo]
                j -= intervalo
            
            vetor[j] = temp
        intervalo //= 2
    return vetor
def merge_sort(vetor):
    if len(vetor) > 1:
        divisao = len(vetor) // 2
        esquerda = vetor[:divisao]
        direita = vetor[divisao:]
        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k= 0

        while i < len(esquerda) and j > len(direita):
            if esquerda[i] < direita[j]:
                vetor[k] = esquerda[i]
                i += 1
            else:
                vetor[k] = direita[j]
                j +=1
            k +=1
        while i < len(esquerda):
            vetor[k] = esquerda[i]
            i+=1
            k+=1
        while j < len(direita):
            vetor[k] = direita[j]
            j +=1
            k +=1
    return vetor
        

def particao(vetor, inicio, final):
    pivo = vetor[final]
    i = inicio -1

    for j in range(inicio, final):
        if vetor[j] <= pivo:
            i+= 1
            vetor[i], vetor[j] = vetor[j], vetor[i+1]
    vetor[i+1], vetor[final] = vetor[final], vetor[i+1]
    return i +1
def quick_sort(vetor, inicio, final):
    if inicio< final:
        posicao = particao(vetor,inicio,final)
        quick_sort(vetor, inicio, posicao -1)

        quick_sort(vetor,posicao +1, final)
    return vetor

# Testes
print("Bubble Sort:", bubble_sort(np.array([1, 2, 3, 4])))
print("Selection Sort:", selection_sort(np.array([1, 23, 5, 2, 6, 235, 6241])))
print("Insertion Sort:", insertion_sort(np.array([24, 231, 535, 6325, 646, 12])))
print("Shell Sort:", shell_sort(np.array([24, 231, 535, 6325, 646, 12, 1])))
print("Merge Sort:", merge_sort(np.array([12, 21, 5, 216, 236, 15, 2])))

vetor = np.array([3, 45, 234, 66, 563, 3])
print("Quick Sort:", quick_sort(vetor, 0, len(vetor) - 1))
print()
print()
lista_original = [random.random() for _ in range(5000)]

# Medir o tempo de cada algoritmo
def medir_tempo(algoritmo, vetor, *args):
    antes = tm.time()
    algoritmo(vetor, *args)  # Executa o algoritmo com os argumentos passados
    depois = tm.time()
    return depois - antes

# Testar os algoritmos
print("Tempo de execução dos algoritmos de ordenação:")
print(f"Bubble Sort: {medir_tempo(bubble_sort, lista_original.copy()):.4f} segundos")
print(f"Selection Sort: {medir_tempo(selection_sort, lista_original.copy()):.4f} segundos")
print(f"Insertion Sort: {medir_tempo(insertion_sort, lista_original.copy()):.4f} segundos")
print(f"Shell Sort: {medir_tempo(shell_sort, lista_original.copy()):.4f} segundos")
print(f"Merge Sort: {medir_tempo(merge_sort, lista_original.copy()):.4f} segundos")
print(f"Quick Sort: {medir_tempo(quick_sort, lista_original.copy(), 0, len(lista_original) - 1):.4f} segundos")


