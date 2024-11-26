class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def valid(row, col):
            return (
                0 <= row < ROWS
                and 0 <= col < COLS
                and grid[row][col] == 1
                and (row, col) not in seen
            )

        def dfs(row, col):
            seen.add((row, col))
            area = 1
            for x, y in directions:
                nr, nc = row + x, col + y
                if valid(nr, nc):
                    seen.add((nr, nc))
                    area += dfs(nr, nc)
            return area

        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) not in seen and grid[i][j] == 1:
                    seen.add((i, j))
                    res = max(res, dfs(i, j))
        return res
