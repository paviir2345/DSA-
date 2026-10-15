def bubblesort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


arr = [4, 1, 3, 9, 7]
print(bubblesort(arr))
