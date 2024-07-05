class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        maxq = deque()#storing indexes monotonically decreasing 
        for i in range(len(nums)):
            curr = nums[i]
            while maxq and  curr > nums[maxq[-1]]:
                maxq.pop()
            maxq.append(i)
            if maxq[0] + k == i: # the next condition would already would have happened in the first place when we
                maxq.popleft()
            if i >= k-1: #>= because once window is formed it will be adding 1 element only 
                ans.append(nums[maxq[0]])

        return ans


