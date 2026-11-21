
def buddyStrings(s, goal):

    if len(s) != len(goal):
        return False

    if s == goal:

        for i in range(len(s)):
            for j in range(i + 1, len(s)):

                if s[i] == s[j]:
                    return True

        return False

    first = -1
    second = -1
    count = 0

    for i in range(len(s)):

        if s[i] != goal[i]:

            count = count + 1

            if count == 1:
                first = i

            elif count == 2:
                second = i

            else:
                return False

    if count == 2:
        if s[first] == goal[second] and s[second] == goal[first]:
            return True

    return False



s = "ab"
goal = "ba"

answer = buddyStrings(s, goal)

print("Output:", answer)
