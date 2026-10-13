def anagram(s, p):
    result = []
    count = {}

    for ch in p:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1

    left = 0

    for right in range(len(s)):
        ch = s[right]

        if ch in count:
            count[ch] -= 1
        else:
            count[ch] = -1

        if right - left + 1 > len(p):
            old = s[left]

            if old in count:
                count[old] += 1

            left += 1

        if right - left + 1 == len(p):
            good = True

            for ch in p:
                if count[ch] != 0:
                    good = False

            if good:
                result.append(left)

    return result


s = "cbaebabacd"
p = "abc"

print(anagram(s, p))