pick = 6

def guess(num):
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guessNumber(n):
    left = 1
    right = n

    while left <= right:
        mid = (left + right) // 2

        result = guess(mid)

        if result == 0:
            return mid
        elif result == 1:
            left = mid + 1
        else:
            right = mid - 1


n = 10
print(guessNumber(n))