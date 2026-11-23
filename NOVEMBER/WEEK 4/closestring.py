class Solution:
    def closeStrings(self, word1, word2):

        if len(word1) != len(word2):
            return False

        a = [0] * 26
        b = [0] * 26

        for ch in word1:
            a[ord(ch) - 97] += 1

        for ch in word2:
            b[ord(ch) - 97] += 1

        for i in range(26):
            if (a[i] == 0 and b[i] != 0) or (a[i] != 0 and b[i] == 0):
                return False

        a.sort()
        b.sort()

        if a == b:
            return True

        return False


word1 = "abc"
word2 = "bca"

obj = Solution()
print(obj.closeStrings(word1, word2))

