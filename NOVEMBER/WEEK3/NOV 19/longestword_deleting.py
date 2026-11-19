
def is_subsequence(word, s):
    i = 0
    j = 0

    while i < len(word) and j < len(s):

        if word[i] == s[j]:
            i = i + 1

        j = j + 1

    return i == len(word)


def find_longest_word(s, dictionary):
    answer = ""

    for i in range(len(dictionary)):

        word = dictionary[i]

        if is_subsequence(word, s):

            if len(word) > len(answer):
                answer = word

            elif len(word) == len(answer) and word < answer:
                answer = word

    return answer


s = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]

print(find_longest_word(s, dictionary))
