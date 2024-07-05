class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc = deque()
        dec = deque()
        left = ans = 0
        
        for right in range(len(nums)):
            curr = nums[right]

            while inc and inc[-1] > curr:
                inc.pop()
            while dec and dec[-1] < curr:
                dec.pop()

            inc.append(curr)
            dec.append(curr)

            while dec[0] - inc[0] > limit:
                if dec[0] == nums[left]:
                    dec.popleft()
                if inc[0] == nums[left]:
                    inc.popleft()
                left += 1
            ans = max(ans,right-left+1)
            
        return ans

            

