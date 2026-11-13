def is_isomorphic(s, t):

    for i in range(len(s)):
        for j in range(i + 1, len(s)):

            if s[i] == s[j] and t[i] != t[j]:
                return False

            if s[i] != s[j] and t[i] == t[j]:
                return False

    return True


s = "egg"
t = "add"

print(is_isomorphic(s, t))