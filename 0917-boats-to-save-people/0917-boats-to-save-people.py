class Solution:
    def numRescueBoats(self, arr: List[int], limit: int) -> int:
        n = len(arr)
        i = 0 
        j = n - 1
        ans = 0
        arr = sorted(arr)
        while i <= j :
            if (arr[i] + arr [j]) > limit:
                ans += 1
                j -= 1
            else:
                ans += 1
                i += 1
                j -= 1
        return ans
