class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        s_row, s_col = entrance
        seen = {(s_row, s_col)}
        queue = deque([(s_row, s_col, 0)])

        def valid(r, c):
            return (
                0 <= r < ROWS
                and 0 <= c < COLS
                and (r, c) not in seen
                and maze[r][c] == "."
            )

        def checkend(r, c):
            return (r in {0, ROWS - 1} or c in {0, COLS - 1}) and (r, c) != (
                s_row,
                s_col,
            )

        while queue:
            row, col, steps = queue.popleft()
            if checkend(row, col):
                return steps
            for x, y in directions:
                nr, nc = row + x, col + y
                if valid(nr,nc):
                    seen.add((nr,nc))
                    queue.append((nr,nc,steps+1))
        return -1
