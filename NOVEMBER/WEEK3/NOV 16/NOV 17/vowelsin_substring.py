
def vowelStrings(words, queries):
    n = len(words)

    prefix = [0] * (n + 1)

    for i in range(n):
        word = words[i]

        if word[0] in "aeiou" and word[len(word) - 1] in "aeiou":
            prefix[i + 1] = prefix[i] + 1
        else:
            prefix[i + 1] = prefix[i]

    result = [0] * len(queries)

    for i in range(len(queries)):
        left = queries[i][0]
        right = queries[i][1]

        result[i] = prefix[right + 1] - prefix[left]

    return result


# Main program
words = ["aba", "bcb", "ece", "aa", "e"]
queries = [[0, 2], [1, 4], [1, 1]]

answer = vowelStrings(words, queries)

print("Output:", answer)
