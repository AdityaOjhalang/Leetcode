class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for row in range(9):
            for col in range(9):
                curr = board[row][col]
                if(curr == "."):
                    continue

                if curr in rows[row] or curr in cols[col] or curr in box[row//3,col//3]:
                    return False
                
                rows[row].add(curr)
                cols[col].add(curr)
                box[row//3,col//3].add(curr)
        
        return True