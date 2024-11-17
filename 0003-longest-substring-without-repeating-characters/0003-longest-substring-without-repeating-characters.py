class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charindx = {}
        low = 0
        maxsize = float("-inf")
        n = len(s)

        for high in range(n):
            curr = s[high]

            if curr in charindx and charindx[curr] >= low:
                low = charindx[curr] + 1
            
            charindx[curr] = high
            maxsize = max(maxsize , high - low + 1)

        return maxsize