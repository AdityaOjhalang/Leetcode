class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        lmax,rmax = 0,0
        for i in range(n):
            #odd
            l,r = i,i
            while l >= 0  and r < n and s[l] == s[r]:
                if (rmax-lmax)+1 <= (r - l) + 1:
                    lmax = l
                    rmax = r
                l-=1
                r+=1
            #even
            l,r = i,i+1
            while l >= 0  and r < n and s[l] == s[r]:
                if (rmax-lmax)+1 <= (r - l) + 1:
                    lmax = l
                    rmax = r
                l-=1
                r+=1
        
        return s[lmax:rmax+1] if s else None