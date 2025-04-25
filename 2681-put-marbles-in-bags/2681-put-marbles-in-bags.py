class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
            
        n = len(weights)

        pairs = [ weights[i] + weights[i+1] for i in range(n-1)]
        pairs.sort()

        minsum = sum(pairs[:k-1])
        maxsum = sum(pairs[-(k-1):])

        return maxsum - minsum