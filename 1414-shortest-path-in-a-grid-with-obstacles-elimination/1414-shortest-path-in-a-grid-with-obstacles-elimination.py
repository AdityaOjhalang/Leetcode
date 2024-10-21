class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        m = len(grid)
        n = len(grid[0])
        queue = deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:
            row, col, rem, steps = queue.popleft()

            if row == m-1 and col == n-1:
                return steps

            for x, y in directions:
                nextr, nextc = x + row, y + col

                if valid(nextr, nextc):

                    if (nextr, nextc, rem) not in seen and grid[nextr][nextc] == 0:
                        seen.add((nextr, nextc,rem))
                        queue.append((nextr, nextc, rem, steps + 1))
                    
                    elif (nextr,nextc, rem -1 ) not in seen and rem:
                        seen.add((nextr, nextc, rem-1))
                        queue.append((nextr, nextc, rem-1, steps + 1))
        return -1
