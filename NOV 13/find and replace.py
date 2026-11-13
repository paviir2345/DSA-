def match_pattern(word, pattern):

    for i in range(len(pattern)):
        for j in range(i + 1, len(pattern)):

            if pattern[i] == pattern[j] and word[i] != word[j]:
                return False

            if pattern[i] != pattern[j] and word[i] == word[j]:
                return False

    return True


def find_and_replace(words, pattern):

    answer = []

    for i in range(len(words)):
        if match_pattern(words[i], pattern):
            answer.append(words[i])

    return answer


words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
pattern = "abb"

print(find_and_replace(words, pattern))