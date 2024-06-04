class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        n = len(s)
        ans = ""
        for i in range(n-1,-1,-1):
            ans+=s[i] + " "

        
        return ans.strip()
        