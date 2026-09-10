class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # approach: every encounter of val, replace it with the next valid element from the
        # back of the array
        i = 0
        n = len(nums)
        while i < n:
            # even if the last element is val, in the next loop, it will decrement again
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n

# Runtime O(n)
# Space O(1) in place
