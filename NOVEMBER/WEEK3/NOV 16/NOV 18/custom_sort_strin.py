
def customSortString(order, s):
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

    result = ""

   
    for ch in order:

        for i in range(len(chars)):

            if chars[i] == ch:

                for j in range(counts[i]):
                    result = result + ch

                counts[i] = 0

    
    for i in range(len(chars)):

        for j in range(counts[i]):
            result = result + chars[i]

    return result



order = "cba"
s = "abcd"

answer = customSortString(order, s)

print("Output:", answer)
