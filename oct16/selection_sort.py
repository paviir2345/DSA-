def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        small = i

        for j in range(i + 1, n):
            if arr[j] < arr[small]:
                small = j

        temp = arr[i]
        arr[i] = arr[small]
        arr[small] = temp

    return arr


arr = [4, 1, 3, 9, 7]
print(selection_sort(arr))