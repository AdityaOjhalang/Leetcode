class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)
        reduction = 0
        res = 0
        for val in ordered:
            reduction += val
            res += 1
            if reduction >= len(arr)/2 :
                break
        return res