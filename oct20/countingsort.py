def countingsort(s):
    count = [0] * 26

    for ch in s:
        count[ord(ch) - ord('a')] += 1

    result = ""

    for i in range(26):
        while count[i] > 0:
            result += chr(i + ord('a'))
            count[i] -= 1

    return result


s = "edsab"
print(countingsort(s))
