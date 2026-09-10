class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #instantly return false if the lens does not equal
        if len(s1) + len(s2) != len(s3):
            return False

        #create a len(s1) + 1 x len(s2) + 1 grid that holds boolean values
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]
        #initialize the bottom right corner as True
        dp[len(s1)][len(s2)] = True

        #bottom up approach
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                #if we take the char from s1, can we make the rest of the string with the remaining from s1 and s2
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                #if we take the char from s2, can we make the rest of the string with the remaining from s1 and s2
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True
        #if the top left corner is true, then we know the string can be made
        return dp[0][0]