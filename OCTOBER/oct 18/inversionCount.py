def inversionCount(arr):
    def merge(a):
        if len(a) <= 1:
            return a, 0

        m = len(a) // 2
        l, x = merge(a[:m])
        r, y = merge(a[m:])

        res = []
        i = j = 0
        count = x + y

        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                count += len(l) - i
                j += 1

        res += l[i:] + r[j:]
        return res, count

    return merge(arr)[1]


print(inversionCount([2, 4, 1, 3, 5]))