class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def valid(row,col):
            return  0 <= row < m and 0 <= col < n

        def check(row,col,mid,seen):
            if row == m-1 and col == n-1:
                return True
            seen.add((row,col))
            for x,y in directions:
                nr,nc = row + x , col + y
                if valid(nr,nc) and (nr,nc) not in seen:
                    if abs(heights[row][col] - heights[nr][nc] ) <= mid:
                        if check(nr,nc,mid,seen):
                            return True 
            return False 

        left, right = 0, max(max(row) for row in heights)
        while left < right:
            mid = (left + right) // 2
            if check(0, 0, mid, set()):  # Use a set to track visited cells
                right = mid 
            else:
                left = mid + 1
        
        return right



            


