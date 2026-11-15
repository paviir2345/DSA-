def merge_sortedarrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    temp = []
    i = 0
    j = 0

    # Merge both sorted arrays
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            temp.append(arr1[i])
            i += 1
        else:
            temp.append(arr2[j])
            j += 1

    while i < n:
        temp.append(arr1[i])
        i += 1

    while j < m:
        temp.append(arr2[j])
        j += 1

    # Divide elements between both arrays
    for i in range(n):
        arr1[i] = temp[i]

    for j in range(m):
        arr2[j] = temp[n + j]


arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

merge_sortedarrays(arr1, arr2)

print("arr1:", arr1)
print("arr2:", arr2)
