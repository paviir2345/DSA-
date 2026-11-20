
class Solution:
    def longestNiceSubstring(self, s):

        longest = ""

        for i in range(len(s)):

            for j in range(i, len(s)):

                sub = s[i:j + 1]
                nice = True

                for ch in sub:

                    if ch.islower():

                        if ch.upper() not in sub:
                            nice = False
                            break

                    else:

                        if ch.lower() not in sub:
                            nice = False
                            break

                if nice == True:

                    if len(sub) > len(longest):
                        longest = sub

        return longest


s = "YazaAay"

obj = Solution()
print(obj.longestNiceSubstring(s))
