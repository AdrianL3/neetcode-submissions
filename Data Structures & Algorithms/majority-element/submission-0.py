class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}

        for num in nums:
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1
        
        currMax = 0
        result = nums[0]

        for key, value in hashMap.items():
            if value > currMax:
                result = key
                currMax = value
        
        return result