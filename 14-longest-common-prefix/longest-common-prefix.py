class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        v = sorted(v)
        ans=""
        first = v[0]
        last = v[-1]
        for i in range(min(len(first),len(last))):
            if(first[i] != last[i]):
                return ans
            else:
                ans+=last[i]
        
        return ans
