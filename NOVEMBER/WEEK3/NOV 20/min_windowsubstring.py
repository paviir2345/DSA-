
class Solution:
    def minWindow(self, s, t):

        if len(t) > len(s):
            return ""

        need = [0] * 128
        window = [0] * 128

        for ch in t:
            need[ord(ch)] += 1

        left = 0
        count = 0
        start = 0
        min_len = len(s) + 1

        for right in range(len(s)):

            ch = s[right]
            window[ord(ch)] += 1

            if window[ord(ch)] <= need[ord(ch)]:
                count += 1

            while count == len(t):

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                ch = s[left]
                window[ord(ch)] -= 1

                if window[ord(ch)] < need[ord(ch)]:
                    count -= 1

                left += 1

        if min_len == len(s) + 1:
            return ""

        return s[start:start + min_len]


s = "ADOBECODEBANC"
t = "ABC"

obj = Solution()
print(obj.minWindow(s, t))

