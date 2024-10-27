class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        cells = [None]* (n**2 +1)
        columns = list(range(n))
        label = 1
        for row in range(n-1,-1,-1):
            for col in columns:
                cells[label] = (row,col)
                label += 1
            columns.reverse()

        queue = deque([(1, 0)])
        seen = set()
        seen.add(1)

        while queue:
            sqr, moves = queue.popleft()

            for i in range(1, 7):
                nextsq = sqr + i
                r, c = cells[nextsq]
                if board[r][c] != -1:
                    nextsq = board[r][c]
                if nextsq == n * n:
                    return moves + 1
                if nextsq not in seen:
                    seen.add(nextsq)
                    queue.append((nextsq, moves + 1))
        return -1
