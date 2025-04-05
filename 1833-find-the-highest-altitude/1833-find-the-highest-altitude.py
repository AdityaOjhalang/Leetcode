class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        prefix = [0]
        for i in range(n):
            prefix.append(gain[i] + prefix[-1])
     
        return max(prefix)