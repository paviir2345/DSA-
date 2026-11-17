
def countVowelSubstrings(word):
    n = len(word)
    answer = 0

    for i in range(n):
        a = 0
        e = 0
        v = 0
        o = 0
        u = 0

        for j in range(i, n):

            if word[j] == 'a':
                a = a + 1

            elif word[j] == 'e':
                e = e + 1

            elif word[j] == 'i':
                v = v + 1

            elif word[j] == 'o':
                o = o + 1

            elif word[j] == 'u':
                u = u + 1

            else:
                break

            if a > 0 and e > 0 and v > 0 and o > 0 and u > 0:
                answer = answer + 1

    return answer



word = "aeiou"

answer = countVowelSubstrings(word)

print("Output:", answer)
