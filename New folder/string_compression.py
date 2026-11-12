
def compress(chars):
    result = ""
    i = 0

    while i < len(chars):
        count = 1

        while i + 1 < len(chars) and chars[i] == chars[i + 1]:
            count = count + 1
            i = i + 1

        result = result + chars[i]

        if count > 1:
            result = result + str(count)

        i = i + 1

    return result



chars = ["a", "a", "a", "b", "b", "c"]

answer = compress(chars)
print("Output:", answer)
