def reversewords(s):
    result = ""
    i = len(s) - 1

    while i >= 0:

        
        while i >= 0 and s[i] == " ":
            i = i - 1

        if i < 0:
            break

        end = i

        
        while i >= 0 and s[i] != " ":
            i = i - 1

        word = s[i + 1:end + 1]

        if result == "":
            result = word
        else:
            result = result + " " + word

    return result


s = "the sky is blue"
print(reversewords(s))