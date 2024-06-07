class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return t

        countT = Counter(t)
        currWindow = {}

        l=0

        have , need = 0 , len(countT)

        res , resLen = [-1,-1] , float("infinity")

        for r in range (len(s)):
            curr = s[r]
            currWindow[curr] = 1 + currWindow.get(curr,0)
            if curr in countT and currWindow[curr] == countT[curr]:
                have +=1
            
            while ( have == need ):

                topop = s[l]

                if r - l + 1 < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                currWindow[topop] -= 1
                if(topop in countT and currWindow[topop] < countT[topop] ):
                    have -= 1
                l+=1
        
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ""