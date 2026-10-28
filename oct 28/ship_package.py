
def ship_package(arr, d):
    left = max(arr)
    right = sum(arr)

    while left <= right:
        mid = (left + right) // 2

        days = 1
        current_weight = 0

        for weight in arr:
            if current_weight + weight <= mid:
                current_weight = current_weight + weight
            else:
                days = days + 1
                current_weight = weight

        if days <= d:
            right = mid - 1
        else:
            left = mid + 1

    return left


arr = [1, 2, 1]
d = 2
print(ship_package(arr, d))
