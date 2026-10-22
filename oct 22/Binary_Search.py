def Binary_Search(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            return mid

        elif arr[mid] < k:
            left = mid + 1

        else:
            right = mid - 1

    return -1


arr = [1, 2, 3, 4, 6]
k = 6

ans = Binary_Search(arr, k)
print(ans)

    