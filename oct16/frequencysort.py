def frequencysort(s):
    chars = list(set(s))

    for i in range(len(chars)):
        for j in range(i + 1, len(chars)):
            if s.count(chars[i]) > s.count(chars[j]) or (s.count(chars[i]) == s.count(chars[j]) and chars[i] > chars[j]):
                chars[i], chars[j] = chars[j], chars[i]

    result = ""
    for ch in chars:
        result += ch * s.count(ch)

    return result


s = "geeksforgeeks"
print(frequencysort(s))