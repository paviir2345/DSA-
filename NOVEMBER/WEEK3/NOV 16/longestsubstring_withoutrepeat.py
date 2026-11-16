def lengthOfLongestSubstring(s):

    count = [0] * 128

    left = 0
    max_length = 0

    for right in range(len(s)):

        ch = ord(s[right])

        count[ch] += 1

        while count[ch] > 1:

            old = ord(s[left])

            count[old] -= 1

            left += 1

        length = right - left + 1

        if length > max_length:
            max_length = length

    return max_length


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))