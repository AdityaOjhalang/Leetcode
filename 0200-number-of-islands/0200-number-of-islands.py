class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == "1"

        def dfs(row, col):
            for x, y in directions:
                next_r, next_c = row + x, col + y
                if valid(next_r,next_c) and (next_r,next_c) not in seen:
                    seen.add((next_r,next_c))
                    dfs(next_r,next_c)

        ans = 0
        m = len(grid)
        n = len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in seen:
                    seen.add((i,j))
                    ans+=1
                    dfs(i,j)
        return ans

