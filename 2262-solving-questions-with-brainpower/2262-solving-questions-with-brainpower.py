class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def dp(i):
            if i >= len(questions):
                return 0
            return max(questions[i][0] + dp(i + questions[i][1] + 1), dp(i+1))
        
        return dp(0)
