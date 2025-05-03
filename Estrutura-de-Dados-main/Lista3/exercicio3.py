import random
import time
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def measure_time(func, arr):
    start = time.time()
    func(arr.copy())
    end = time.time()
    return end - start

sizes = [1000, 10000, 20000, 30000, 40000, 50000]
algorithms = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quicksort
}

data = []

for size in sizes:
    base_list = random.sample(range(size * 10), size)
    for name, func in algorithms.items():
        if name in ["Bubble Sort", "Selection Sort", "Insertion Sort"] and size > 10000:
            continue  # Pula algoritmos lentos para listas grandes
        tempo = measure_time(func, base_list)
        data.append({"Algoritmo": name, "Tamanho": size, "Tempo": tempo})

# Lista descendente com 50.000 elementos
desc_list = list(range(50000, 0, -1))
for name, func in algorithms.items():
    if name in ["Bubble Sort", "Selection Sort", "Insertion Sort"]:
        continue
    tempo = measure_time(func, desc_list)
    data.append({"Algoritmo": name + " (Desc)", "Tamanho": 50000, "Tempo": tempo})

df = pd.DataFrame(data)

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="Tamanho", y="Tempo", hue="Algoritmo", marker="o")
plt.title("Comparação de Algoritmos de Ordenação")
plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo de Execução (s)")
plt.grid(True)
plt.tight_layout()
plt.show()
