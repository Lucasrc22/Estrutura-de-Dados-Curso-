import time
import random



def quicksort_pior(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x < pivot]
    right = [x for x in arr[:-1] if x >= pivot]
    return quicksort_pior(left) + [pivot] + quicksort_pior(right)


def quicksort_melhor(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_melhor(left) + mid + quicksort_melhor(right)


n = 100  

lista_ordenada = list(range(n))               
lista_aleatoria = random.sample(range(n), n)  

inicio_pior = time.time()
quicksort_pior(lista_ordenada)
fim_pior = time.time()



inicio_melhor = time.time()
quicksort_melhor(lista_aleatoria)
fim_melhor = time.time()



print(f"Tempo de execução (pior caso - lista ordenada): {fim_pior - inicio_pior:.5f} segundos")
print(f"Tempo de execução (melhor caso - lista aleatória): {fim_melhor - inicio_melhor:.5f} segundos")
