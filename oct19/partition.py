def partition(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return partition(less) + equal + partition(greater)


arr = [4, 2, 4, 1, 2]
print(partition(arr))