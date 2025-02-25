class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charind = {}
        start = 0
        res = 0
        for end in range(len(s)):
            char = s[end]
            while char in charind and charind[char] >= start:
                start += 1
            charind[char] = end
            res = max(res,end-start+1)
        return res