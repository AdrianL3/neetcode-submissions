import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)

        while lower <= upper:
            mid = (lower + upper) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            
            if hours > h:
                lower = mid + 1
            if hours <= h:
                upper = mid - 1

        return lower