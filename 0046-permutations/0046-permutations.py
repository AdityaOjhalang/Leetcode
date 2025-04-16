class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path,used):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for num in nums:
                if num not in used:
                    used.add(num)
                    path.append(num)
                    backtrack(path,used)
                    used.remove(num)
                    path.pop()
        res = []
        backtrack([],set())
        return res 
