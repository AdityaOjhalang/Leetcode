class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas_sum = sum(gas)
        cost_sum = sum(cost)
        total=0
        start=0
        if(gas_sum < cost_sum):
                return -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if(total<0):
                total=0
                start = i+1
        
        return start
        