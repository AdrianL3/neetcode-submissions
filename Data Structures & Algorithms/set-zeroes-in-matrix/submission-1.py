class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        #work our way top to bottom left to right
        # O(1) memory solution
        rows, cols = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows and columns need to be zero
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    #if there is a zero, make the first element in the column (the top)
                    #to zero to indicate that the col needs to be zero
                    matrix[0][c] = 0
                    
                    #update the row indicator
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = True

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(rows):
                matrix[r][0] = 0
        
        if rowZero:
            for c in range(cols):
                matrix[0][c] = 0


