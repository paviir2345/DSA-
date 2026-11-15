def repeatedSubstringPattern(s):

    n = len(s)

    for i in range(1, n // 2 + 1):

        if n % i == 0:

            part = ""

            for j in range(i):
                part = part + s[j]

            result = ""

            for j in range(n // i):
                result = result + part

            if result == s:
                return True

    return False


print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabc"))
