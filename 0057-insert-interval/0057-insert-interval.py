class Solution:
    def insert(self, intervals: List[List[int]], new: List[int]) -> List[List[int]]:
        res = []
        for i , intl in enumerate(intervals):
            #new interval is smaller
            if new[1] < intl[0]:
                res.append(new)
                return res + intervals[i:]

            #new interval is bigger
            elif intl[1] < new[0]:
                res.append(intl)

            else:
            #new interval is merging 
                new[0] = min(new[0],intl[0])
                new[1] = max(new[1],intl[1])

        res.append(new)
        return res
        


