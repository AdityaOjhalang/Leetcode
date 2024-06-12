class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        def countNeighbours(r,c):
            nei = 0
            for dr , dc in neighbors:
                nr , nc = r + dr , c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] in [1,3]:
                    nei += 1
            return nei
        
        for r in range(ROWS):
            for c in range(COLS):
                live = countNeighbours(r,c)
                if board[r][c] == 1 and ( live in [2,3]):
                    board[r][c] = 3
                if board[r][c] == 0 and ( live == 3):
                    board[r][c] = 2

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in [2,3]:
                    board[r][c] = 1
                else:
                    board[r][c] = 0                   





