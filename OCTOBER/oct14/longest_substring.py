def longest_substring(s):
    left = 0
    seen = {}
    max_length = 0

    for right in range(len(s)):
        ch = s[right]

        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1

        seen[ch] = right

        length = right - left + 1

        if length > max_length:
            max_length = length

    return max_length


print(longest_substring("abcabcbb"))