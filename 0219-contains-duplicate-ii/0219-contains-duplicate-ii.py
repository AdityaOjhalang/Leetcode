class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dupes = {}

        for i,curr in enumerate(nums):
            if curr in dupes:
                prev = dupes[curr]
                if abs(i-prev) <=k:
                    return True
            dupes[curr] = i
        return False
