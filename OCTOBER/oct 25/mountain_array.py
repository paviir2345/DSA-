
def mountain_array(mountainArr, target):
    left = 0
    right = len(mountainArr) - 1

    while left < right:
        mid = (left + right) // 2

        if mountainArr[mid] < mountainArr[mid + 1]:
            left = mid + 1
        else:
            right = mid

    peak = left

    
    left = 0
    right = peak

    while left <= right:
        mid = (left + right) // 2

        if mountainArr[mid] == target:
            return mid
        elif mountainArr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    
    left = peak + 1
    right = len(mountainArr) - 1

    while left <= right:
        mid = (left + right) // 2

        if mountainArr[mid] == target:
            return mid
        elif mountainArr[mid] < target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


mountainArr = [1, 2, 3, 4, 5, 3, 1]
target = 3

print(mountain_array(mountainArr, target))







  