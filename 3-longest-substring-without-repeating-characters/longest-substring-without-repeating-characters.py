class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charindx = {}
        start = 0
        maxsize = 0
        n = len(s)

        for end in range(len(s)):
            curr = s[end]

            if curr in charindx and charindx[curr] >= start:
                start = charindx[curr] +1
            
            charindx[curr] = end
            maxsize = max(maxsize , end - start + 1 )
        return maxsize

