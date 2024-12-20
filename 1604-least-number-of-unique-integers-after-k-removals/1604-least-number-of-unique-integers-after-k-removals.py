class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)

        while k:
            val = ordered[-1]
            if val <= k:
                ordered.pop()
                k -= val
            else:
                break
        return len(ordered)
