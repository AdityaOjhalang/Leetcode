class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        ROWS, COLS = len(board), len(board[0])
        vistied = set()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def mark(r, c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS) or board[r][c] != "O":
                return
            board[r][c] = "E"
            vistied.add((r,c))
            for x, y in directions:
                nr, nc = x + r, y + c
                mark(nr,nc)

        for r in range(ROWS):
            if board[r][0] == "O":
                mark(r,0)
            if board[r][COLS-1] == "O":
                mark(r,COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                mark(0,c)
            if board[ROWS-1][c] == "O":
                mark(ROWS-1,c)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"
        
