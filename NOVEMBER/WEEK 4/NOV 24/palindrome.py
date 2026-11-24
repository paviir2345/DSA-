
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left = left + 1
        right = right - 1

    return True


def longest_palindrome(s):
    answer = ""

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]

            if is_palindrome(sub):
                if len(sub) > len(answer):
                    answer = sub

    return answer


s = "babad"
print(longest_palindrome(s))
