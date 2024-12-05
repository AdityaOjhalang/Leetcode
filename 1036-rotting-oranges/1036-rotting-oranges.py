class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        totalFresh = 0
        queue = deque()

        def valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == ROTTEN:
                    queue.append((i, j))
                elif grid[i][j] == FRESH:
                    totalFresh += 1

        if totalFresh == 0:
            return 0

        nummins = -1
        while queue:
            nummins += 1
            num = len(queue)
            for _ in range(num):
                r, c = queue.popleft()
                for x, y in directions:
                    nr, nc = r + x, c + y
                    if valid(nr,nc) and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        totalFresh -= 1
                        queue.append((nr,nc))

        if totalFresh == 0:
            return nummins
        else:
            return -1 
