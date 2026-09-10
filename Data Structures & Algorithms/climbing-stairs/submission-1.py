class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        #need a dp array with n+1 slots
        dp = [0] * (n+1)
        #initialize dp1 and dp 2
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            #fibonaci addition, add the total ways for the previous step and 2 previous steps
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]