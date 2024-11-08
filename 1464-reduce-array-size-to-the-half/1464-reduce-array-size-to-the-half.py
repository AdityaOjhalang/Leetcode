class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)
        n = len(arr)/2
        print(ordered)
        reduction = 0
        res = 0
        for val in ordered:
            reduction += val
            res += 1
            if reduction >= n:
                break
        return res