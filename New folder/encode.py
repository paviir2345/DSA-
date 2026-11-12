
def encode(words):
    result = ""

    for word in words:
        result = result + str(len(word)) + "#" + word

    return result


def decode(s):
    result = []
    i = 0

    while i < len(s):
        count = 0

        while s[i] != "#":
            count = count * 10 + int(s[i])
            i = i + 1

        i = i + 1
        word = ""

        for j in range(count):
            word = word + s[i]
            i = i + 1

        result = result + [word]

    return result


# Main program
words = ["cat", "dog"]

encoded = encode(words)
print("Encoded:", encoded)

decoded = decode(encoded)
print("Decoded:", decoded)
