class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1

            target = -1 * nums[i]
            while j < k:
                currSum = nums[j] + nums[k]

                if currSum < target:
                    j += 1
                elif currSum > target:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    # move from duplicate next j vals
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return result