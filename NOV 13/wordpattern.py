def word_pattern(pattern, s):

    words = s.split()

    if len(pattern) != len(words):
        return False

    for i in range(len(pattern)):
        for j in range(i + 1, len(pattern)):

            if pattern[i] == pattern[j] and words[i] != words[j]:
                return False

            if pattern[i] != pattern[j] and words[i] == words[j]:
                return False

    return True


pattern = "abba"
s = "dog cat cat dog"

print(word_pattern(pattern, s))