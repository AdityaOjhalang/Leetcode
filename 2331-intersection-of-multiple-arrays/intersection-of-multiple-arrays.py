class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)

        for i in nums:
            for x in i:
                counts[x] += 1

        ans = []
        n = len(nums)

        for x in counts:
            if counts[x] == n:
                ans.append(x)
        
        return sorted(ans)
        