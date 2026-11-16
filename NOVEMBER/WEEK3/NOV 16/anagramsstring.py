def findAnagrams(s, p):

    result = []

    if len(p) > len(s):
        return result

    count1 = [0] * 26
    count2 = [0] * 26

    for i in range(len(p)):

        a = ord(p[i]) - ord('a')
        b = ord(s[i]) - ord('a')

        count1[a] += 1
        count2[b] += 1

    if count1 == count2:
        result.append(0)

    left = 0

    for right in range(len(p), len(s)):

        new_char = ord(s[right]) - ord('a')
        count2[new_char] += 1

        old_char = ord(s[left]) - ord('a')
        count2[old_char] -= 1

        left += 1

        if count1 == count2:
            result.append(left)

    return result


print(findAnagrams("cbaebabacd", "abc"))
print(findAnagrams("abab", "ab"))
print(findAnagrams("hello", "ll"))