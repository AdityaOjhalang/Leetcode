class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        def valid(row,col):
            return 0<=row<ROWS and 0<=col<COLS
        
        def backtrack(row,col,i,seen):
            if i == len(word):
                return True
            
            for x,y in directions:
                nr,nc = row+x,col+y
                if valid(nr,nc) and board[nr][nc] == word[i] and (nr,nc) not in seen:
                    seen.add((nr,nc))
                    if backtrack(nr,nc,i+1,seen):
                        return True
                    seen.remove((nr,nc))
            return False
        
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0] and backtrack(row,col,1,{(row,col)}):
                    return True
        return False

                        