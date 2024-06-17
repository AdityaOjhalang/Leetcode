class Solution:
    def countElements(self, arr: List[int]) -> int:
        hset = set(arr)
        count = 0
        for x in arr:
            if x+1 in hset:
                count +=1
        return count