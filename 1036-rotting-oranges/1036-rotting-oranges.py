class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        FRESH, ROTTEN = 1, 2
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        totalfresh = 0
        queue = deque()

        def valid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                if grid[i][j] == FRESH:
                    totalfresh += 1

        if totalfresh == 0:
            return 0
        nummins = -1
        while queue:
            nummins += 1
            tot = len(queue)
            for _ in range(tot):
                row, col = queue.popleft()
                for x, y in directions:
                    nr, nc = row + x, col + y
                    if valid(nr,nc) and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        queue.append((nr,nc))
                        totalfresh -= 1
        if totalfresh == 0:
            return nummins
        else:
            return -1
