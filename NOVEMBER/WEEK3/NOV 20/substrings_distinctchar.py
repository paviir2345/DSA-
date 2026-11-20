
class Solution:
    def countGoodSubstrings(self, s):

        count = 0

        for i in range(len(s) - 2):

            a = s[i]
            b = s[i + 1]
            c = s[i + 2]

            if a != b and b != c and a != c:
                count += 1

        return count


s = "xyzzaz"

obj = Solution()
print(obj.countGoodSubstrings(s))
