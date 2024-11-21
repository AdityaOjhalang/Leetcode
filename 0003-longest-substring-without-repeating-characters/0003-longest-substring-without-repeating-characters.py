class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charind = {}
        start = 0
        res = 0
        for end in range(len(s)):
            curr = s[end]
            while curr in charind and charind[curr] >= start:
                start += 1
            
            charind[curr] = end
            res = max(res,end-start+1)
        print(charind)
        return res

            

