class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for n in nums:
            curr += n % 2
            diff = curr - k
            ans += counts.get(diff,0)
            counts[curr] += 1

        return ans