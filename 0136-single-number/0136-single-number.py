class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        for num,freq in counts.items():
            if freq == 1:
                return num 
        return None 