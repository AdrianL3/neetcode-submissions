class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #iterate through the array, and once we get a negative prefix remove it
        maxSub = nums[0]

        curSum = 0

        for n in nums:
            #if the prefix is less then zero, reset it to 0 to the current index
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        
        return maxSub