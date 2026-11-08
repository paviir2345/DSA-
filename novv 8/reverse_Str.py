def reverseStr(s, k):
    arr = list(s)
    n = len(arr)

    start = 0

    while start < n:

        left = start
        right = start + k - 1

        if right >= n:
            right = n - 1

        while left < right:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1

        start = start + 2 * k

    return "".join(arr)


s = "abcdefg"
k = 2

print(reverseStr(s, k))