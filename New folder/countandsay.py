
def countAndSay(n):
    result = "1"

    for i in range(n - 1):
        new = ""
        j = 0

        while j < len(result):
            count = 1

            while j + 1 < len(result) and result[j] == result[j + 1]:
                count = count + 1
                j = j + 1

            new = new + str(count) + result[j]
            j = j + 1

        result = new

    return result



n = 5

answer = countAndSay(n)
print("Output:", answer)
