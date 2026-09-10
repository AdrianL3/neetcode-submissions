import copy

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = copy.deepcopy(cost)

        for i in range(2, len(cost)):
            dp[i] = min(dp[i] + dp[i-1], dp[i]+ dp[i-2])

        return min(dp[len(cost) - 1], dp[len(cost) - 2])