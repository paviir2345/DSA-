
def countSegments(s):
    count = 0

    for i in range(len(s)):

        if s[i] != " ":

            if i == 0 or s[i - 1] == " ":
                count = count + 1

    return count



s = "Hello my name is John"

answer = countSegments(s)

print("Output:", answer)
