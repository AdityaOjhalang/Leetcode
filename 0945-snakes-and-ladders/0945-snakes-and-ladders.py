class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def pos(square):
            row = (square - 1) // length
            col = (square - 1) % length

            if row%2:
                col = length - 1 - col
            return [row, col]

        queue = deque([(1, 0)])
        seen = set()
        seen.add(1)

        while queue:
            sqr, moves = queue.popleft()

            for i in range(1, 7):
                nextsq = sqr + i
                r, c = pos(nextsq)
                if board[r][c] != -1:
                    nextsq = board[r][c]
                if nextsq == length * length:
                    return moves + 1
                if nextsq not in seen:
                    seen.add(nextsq)
                    queue.append((nextsq, moves + 1))
        return -1
