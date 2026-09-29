class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        result = 0

        while l < r:
            width = r - l
            length = min(heights[l], heights[r])

            volume = length * width

            result = max(result, volume)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return result