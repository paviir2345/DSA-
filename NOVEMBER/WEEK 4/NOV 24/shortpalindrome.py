
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left = left + 1
        right = right - 1

    return True


def shortest_palindrome(s):

    for i in range(len(s), -1, -1):

        prefix = s[:i]

        if is_palindrome(prefix):

            remaining = s[i:]
            front = remaining[::-1]

            return front + s


s = "abcd"
print(shortest_palindrome(s))
