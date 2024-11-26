from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dp(end):
            if end < 0:
                return True

            if end in memo:
                return memo[end]

            for word in wordDict:
                start = end - len(word) + 1
                if start >= 0 and s[start : end + 1] == word and dp(start - 1):
                    memo[end] = True
                    return memo[end]  # Simplified return

            memo[end] = False
            return memo[end]  # Simplified return

        return dp(len(s) - 1)
