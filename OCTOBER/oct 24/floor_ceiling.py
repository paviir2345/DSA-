def floor_ceiling(arr, target):
    floor = -1
    ceil = -1

    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return [target, target]

        elif arr[mid] < target:
            floor = arr[mid]
            left = mid + 1

        else:
            ceil = arr[mid]
            right = mid - 1

    return [floor, ceil]


arr = [1, 2, 4, 6, 8]
target = 5

print(floor_ceiling(arr, target))
