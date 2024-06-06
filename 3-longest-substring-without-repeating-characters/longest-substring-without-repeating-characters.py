class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charindx = {}
        start = 0
        maxsize = 0

        for end in range(len(s)):
            current = s[end]

            if current in charindx and charindx[current] >= start:
                start = charindx[current]+1
            
            charindx[current] = end 
            maxsize = max(maxsize , end-start+1)
        
        return maxsize