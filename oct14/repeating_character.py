def repeating_character(s, k):
    count = {}
    left = 0
    max_freq = 0
    answer = 0

    for right in range(len(s)):
        ch = s[right]

        if ch not in count:
            count[ch] = 0
        count[ch] += 1

        if count[ch] > max_freq:
            max_freq = count[ch]

        if right - left + 1 - max_freq > k:
            count[s[left]] -= 1
            left += 1

        length = right - left + 1

        if length > answer:
            answer = length

    return answer


print(repeating_character("AABABBA", 1))