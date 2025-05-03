#Questão para eu explicar

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):

        swapped = False

        for j in range(0, n - i -1):

            if arr[j] > arr[j +1]:
                arr[j], arr[j +1] = arr[j +1], arr[j]

                swapped = True
            
        if not swapped:
            break

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        current_value = arr[i]
        j = i -1

        while j >= 0 and arr[j] > current_value:
            arr[j +1] = arr[j]

            j -= 1

        arr[j + 1] = current_value
    
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left, right):
    merged = []

    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index +=1
        
        else:
            merged.append(right[right_index])
            right_index +=1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

def quicksort(arr):
    if len(arr) <=1:
        return arr

    else:
        pivot =- arr[len(arr) // 2]

        left = [x for x in arr if x < pivot]

        middle = [x for x in arr if x == pivot]

        right = [x for x in arr if x > pivot]

        return quicksort(left) + middle + quicksort(right)