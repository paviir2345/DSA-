def sort(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left] = 0
            arr[right] = 1
            left += 1
            right -= 1

    return arr


arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print(sort(arr))
