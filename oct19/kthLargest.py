
def partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def kthLargest(arr, k):
    n = len(arr)
    target = n - k

    low = 0
    high = n - 1

    while low <= high:
        p = partition(arr, low, high)

        if p == target:
            return arr[p]
        elif p < target:
            low = p + 1
        else:
            high = p - 1


arr = [3, 5, 4, 2, 9]
k = 3

print(kthLargest(arr, k))
