def shell_sort(arr):
    n = len(arr)
    gap = n // 2  

    while gap > 0:
        
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2

    return arr

lista = [23, 12, 1, 8, 34, 54, 2, 3]
print("Original:", lista)
ordenada = shell_sort(lista.copy())
print("Ordenada:", ordenada)
