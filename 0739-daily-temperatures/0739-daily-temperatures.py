class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack_indx = []
        ans = [0]*len(temperatures)
        for currday in range(len(temperatures)):
            while stack_indx and temperatures[stack_indx[-1]] < temperatures[currday]:
                previousday = stack_indx.pop()
                ans[previousday] = currday - previousday
            
            stack_indx.append(currday)
        return ans
