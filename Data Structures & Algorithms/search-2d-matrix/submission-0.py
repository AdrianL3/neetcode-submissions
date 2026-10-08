class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        searchIndex = -1

        while l <= r:
            mid = (l + r) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                searchIndex = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1

        if searchIndex == -1:
            return False
        
        searchArray = matrix[searchIndex]
        l, r = 0, len(searchArray) - 1
        

        while l <= r:
            mid = (l + r) // 2

            if searchArray[mid] > target:
                r = mid - 1
            elif searchArray[mid] < target:
                l = mid + 1
            else:
                return True
        
        return False
