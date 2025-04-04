class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hmap = defaultdict(int)
        res = 0
        for n in nums:
            compl = k - n
            if hmap[compl] > 0:
                hmap[compl] -= 1
                res += 1
            else:
                hmap[n] += 1
        return res 

            