class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gsum = sum(gas)
        csum = sum(cost)
        if gsum < csum:
            return -1
        start = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                start = i +1
                total = 0
        return start