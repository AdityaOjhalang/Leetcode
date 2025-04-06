class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        rowset = defaultdict(int)

        # Store row indices for each unique row (converted to tuple)
        for i in range(m):
            row_tuple = tuple(grid[i])
            rowset[row_tuple] += 1

        res = 0
        # Build each column as a tuple and count matching rows
        for j in range(n):
            col = []
            for i in range(m):
                col.append(grid[i][j])
            col_tuple = tuple(col)
            res += rowset[col_tuple]

        return res
