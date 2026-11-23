
def areAlmostEqual(s1, s2):

    first = -1
    second = -1
    count = 0

    for i in range(len(s1)):

        if s1[i] != s2[i]:

            count += 1

            if count == 1:
                first = i

            elif count == 2:
                second = i

            else:
                return False

    if count == 0:
        return True

    if count == 2:

        if s1[first] == s2[second] and s1[second] == s2[first]:
            return True

    return False


s1 = "bank"
s2 = "kanb"

print(areAlmostEqual(s1, s2))
