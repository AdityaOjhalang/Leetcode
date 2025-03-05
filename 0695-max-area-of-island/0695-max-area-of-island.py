class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        seen = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        def valid(r,c):
            return 0 <= r < ROWS and 0 <= c < COLS
        def dfs(row,col):
            area = 1
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc) and (nr,nc) not in seen and grid[nr][nc] == 1:
                    seen.add((nr,nc))
                    area += dfs(nr,nc)
            return area
        maxarea = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i,j) not in seen:
                    seen.add((i,j))
                    area = dfs(i, j)
                    maxarea = max(area, maxarea)
        return maxarea


