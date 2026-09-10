class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #use DFS to run on each of the edges of the pacific and atlantic
        #store the results into a hash set where the values are the coordinates
        #all values in both the pacific and atlantic sets are in the result
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            #if the value is in visit, or out of bounds, or on the edge, 
            #or the value is shorter than the other
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r,c))

            #run dfs on all 4 of its neighbors
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
                
        #top and bottom edge
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
    
        #left and right edge
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res


