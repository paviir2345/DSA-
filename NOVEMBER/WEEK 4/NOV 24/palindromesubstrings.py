
def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left = left + 1
        right = right - 1

    return True


def count_substrings(s):
    count = 0

    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]

            if is_palindrome(sub):
                count = count + 1

    return count


s = "aaa"
print(count_substrings(s))
