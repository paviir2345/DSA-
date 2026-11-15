def isBadVersion(version):
    if version >= 4:
        return True
    else:
        return False


def firstBadVersion(n):
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2

        if isBadVersion(mid):
            right = mid
        else:
            left = mid + 1

    return left


n = 5
print(firstBadVersion(n))