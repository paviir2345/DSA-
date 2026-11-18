
def reorganizeString(s):
    chars = []
    counts = []

    
    for ch in s:
        found = False

        for i in range(len(chars)):
            if chars[i] == ch:
                counts[i] = counts[i] + 1
                found = True
                break

        if found == False:
            chars = chars + [ch]
            counts = counts + [1]

    
    maximum = 0

    for i in range(len(counts)):
        if counts[i] > maximum:
            maximum = counts[i]

    if maximum > (len(s) + 1) // 2:
        return ""

    
    result = ""

    for i in range(len(s)):
        best = -1
        highest = 0

        for j in range(len(chars)):

            if counts[j] > highest:

                if i == 0 or chars[j] != result[i - 1]:
                    highest = counts[j]
                    best = j

        if best == -1:
            return ""

        result = result + chars[best]
        counts[best] = counts[best] - 1

    return result


s = "aab"

answer = reorganizeString(s)

print("Output:", answer)
