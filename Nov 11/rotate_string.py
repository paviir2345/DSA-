def rotateString(s, goal):
    if len(s) != len(goal):
        return False

    n = len(s)

    for i in range(n):
        match = True

        for j in range(n):
            if s[(i + j) % n] != goal[j]:
                match = False
                break

        if match:
            return True

    return False


s = "abcde"
goal = "cdeab"

print(rotateString(s, goal))