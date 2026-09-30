class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        result = 0

        for i in range(len(prices)):
            if prices[i] > currMin:
                result = max(result, prices[i] - currMin)
            if prices[i] < currMin:
                currMin = prices[i]

        return result