
def optimized_bubblesort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if swapped == False:
            break

    return arr


arr = [1, 2, 3, 4, 5]
print(optimized_bubblesort(arr))
