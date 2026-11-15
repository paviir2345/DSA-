def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1


def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)

        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


arr = [4, 1, 3, 9, 7]

quicksort(arr, 0, len(arr) - 1)
print(arr)
