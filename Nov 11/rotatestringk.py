def rotateByK(s, k):
    n = len(s)

    if n == 0:
        return s

    k = k % n
    result = ""

    for i in range(n):
        index = (i - k) % n
        result = result + s[index]

    return result


s = "abcdef"
k = 2

print(rotateByK(s, k))