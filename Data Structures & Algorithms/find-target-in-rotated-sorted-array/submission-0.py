class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find pivot with binary search
        l , r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot = l 

        #initalize new l and r pointers to the section in which the target will be

        l , r = 0, len(nums) - 1

        #if the target is bigger than the current pivot and the target is smaller than the right pointer,
        # then the number is in the right section
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        #do binary serach on the new current window
        while l <= r:
            m = ( l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1

        #if target is not found
        return -1 