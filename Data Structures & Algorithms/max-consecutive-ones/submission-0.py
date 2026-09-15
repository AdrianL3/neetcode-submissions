class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = j = 0
        result =  0

        # sliding window solution
        while j < len(nums):
            # first case: both i and j are 1s
            if nums[i] == 1 and nums[j] == 1:
                j += 1
                result = max(result, j - i)
                continue
            # 2nd case: j is 0
            if nums[j] == 0:
                j += 1
                i = j
                continue


        return result