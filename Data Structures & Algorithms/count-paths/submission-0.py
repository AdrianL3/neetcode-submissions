class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #init a dp array for the bottom row
        row = [1] * n

        #iterate for each row from the bottom up
        for i in range(m - 1):
            newRow = [1] * n
            #iterating right to left, calculate the number of ways to reach
            #the end for the current position in the row
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]