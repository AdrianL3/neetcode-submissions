class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0 
        n = len(s)

        if not s:
            return result

        for i in range(1, n):
            result += abs(ord(s[i]) - ord(s[i - 1]))

        return result