class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicate first values
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] > 0:
                break
            target = -1 * nums[i]

            l = i + 1
            r = len(nums) - 1

            while l < r:
                currSum = nums[l] + nums[r]
                
                if currSum > target:
                    r -= 1
                elif currSum < target:
                    l += 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # move from duplicate next j vals
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return result
