class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        ROWS = len(board)
        COLS = len(board[0])

        def valid(row,col):
            return 0 <= row < ROWS and 0 <= col < COLS
        
        def backtrack(row,col,seen,i):
            if i == len(word):
                return True
            
            for x,y in directions:
                nr , nc = row + x , col + y
                if valid(nr,nc) and (nr,nc) not in seen and board[nr][nc] == word[i] : #similar to board[r][c] == 0
                        seen.add((nr,nc))
                        if backtrack(nr,nc,seen,i+1):
                            return True
                        seen.remove((nr,nc))
            return False
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0] and backtrack(i,j,{(i,j)},1):
                    return True
        return False

                   
