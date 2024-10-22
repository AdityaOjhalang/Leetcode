class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "."

        def checkend(r, c):
            return (r in {0, m - 1} or c in {0, n - 1}) and (r, c) != (x,y)

        m = len(maze)
        n = len(maze[0])

        x, y = entrance
        queue = deque([(x, y, 0)])
        seen = {(x, y)}

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()

            if checkend(row, col):
                return steps

            for x, y in directions:
                nr, nc = row + x, col + y
                if valid(nr,nc) and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    queue.append((nr,nc,steps+1))
        
        return -1

