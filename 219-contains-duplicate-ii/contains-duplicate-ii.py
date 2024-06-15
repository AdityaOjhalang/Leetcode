class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dupes = {}
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr in dupes:
                sec = dupes[curr]
                if( abs(i - sec) <= k):
                    return True
                else:
                    dupes[curr] = i
            else:
                dupes[curr] = i

        return False
