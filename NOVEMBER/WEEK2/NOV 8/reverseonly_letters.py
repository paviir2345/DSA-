def reverseOnlyLetters(s):
    arr = list(s)

    left = 0
    right = len(arr) - 1

    while left < right:

        if not (('a' <= arr[left] <= 'z') or ('A' <= arr[left] <= 'Z')):
            left = left + 1

        elif not (('a' <= arr[right] <= 'z') or ('A' <= arr[right] <= 'Z')):
            right = right - 1

        else:
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp

            left = left + 1
            right = right - 1

    return "".join(arr)


s = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(s))