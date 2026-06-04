a=[34, 7, 21, 48, 12, 3, 45, 19, 30, 2, 16, 50, 28, 9, 41, 14, 37, 23, 6, 44, 11, 33, 25, 8, 49, 18, 5, 42, 27, 31, 15, 40, 1, 29, 47, 10, 22, 36, 13, 46, 4, 24, 39, 17, 35, 8, 43, 26, 32, 20, 38, 29]

def ordenamiento_binario(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


ordenamiento_binario(a)
print("Lista ordenada:", a)