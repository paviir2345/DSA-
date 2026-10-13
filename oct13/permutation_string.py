def permutation_string(s1, s2):
    size = len(s1)

    if size > len(s2):
        return False

    for i in range(len(s2) - size + 1):
        window = s2[i:i + size]

        if sorted(window) == sorted(s1):
            return True

    return False


s1 = "ab"
s2 = "eidbaooo"

print(permutation_string(s1, s2)) -