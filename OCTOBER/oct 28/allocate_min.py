
def allocate_min(arr, k):
    if k > len(arr):
        return -1

    left = max(arr)
    right = sum(arr)

    while left <= right:
        mid = (left + right) // 2

        students = 1
        pages = 0

        for book in arr:
            if pages + book <= mid:
                pages = pages + book
            else:
                students = students + 1
                pages = book

        if students <= k:
            right = mid - 1
        else:
            left = mid + 1

    return left


arr = [12, 34, 67, 90]
k = 2
print(allocate_min(arr, k))
