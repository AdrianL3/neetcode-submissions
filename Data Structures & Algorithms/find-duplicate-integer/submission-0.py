class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            #get the index of the value in the current iteration
            idx = abs(num) -1

            if nums[idx] < 0:
                #if the idx is negative, then the num has already been visited
                return abs(num)
            nums[idx] *= -1
        return -1