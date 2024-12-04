class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        counts = {'a': 0, 'b': 0, 'c': 0}
        for c in s:
            counts[c] += 1

        if min(counts.values()) < k:
            return -1
        
        #sliding window 
        n = len(s)
        l = 0
        res = float("inf")
        for r in range(len(s)): 
            counts[s[r]] -= 1
            while min(counts.values()) < k:
                counts[s[l]] += 1
                l += 1
            res = min(res, n - (r-l+1))

        return res
