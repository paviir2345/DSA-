def rotateString(s, goal):

    if len(s) != len(goal):
        return False

    for i in range(len(s)):

        rotated = ""

        for j in range(i, len(s)):
            rotated = rotated + s[j]

        for j in range(i):
            rotated = rotated + s[j]

        if rotated == goal:
            return True

    return False


print(rotateString("abcde", "cdeab"))
print(rotateString("abcde", "abced"))