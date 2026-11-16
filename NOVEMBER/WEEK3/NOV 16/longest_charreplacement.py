def characterReplacement(s, k):

    count = [0] * 26

    left = 0
    max_freq = 0
    max_length = 0

    for right in range(len(s)):

        ch = ord(s[right]) - ord('A')

        count[ch] += 1

        if count[ch] > max_freq:
            max_freq = count[ch]

        while (right - left + 1) - max_freq > k:

            old = ord(s[left]) - ord('A')

            count[old] -= 1

            left += 1

        length = right - left + 1

        if length > max_length:
            max_length = length

    return max_length


print(characterReplacement("AABABBA", 1))
print(characterReplacement("ABAB", 2))
print(characterReplacement("AAAA", 2))