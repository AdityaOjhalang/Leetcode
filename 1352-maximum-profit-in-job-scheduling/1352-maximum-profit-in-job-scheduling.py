class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # Convert zip to list and sort by end time
        jobs = list(zip(startTime, endTime, profit))
        jobs = sorted(jobs, key=lambda x: x[1])

        @cache
        def dp(i):
            if i < 0:
                return 0
            
            # Binary search to find last non-overlapping job
            lo, hi = 0, i - 1
            last = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if jobs[mid][1] <= jobs[i][0]:
                    last = mid
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            skip = dp(i - 1)
            take = jobs[i][2] + dp(last)
            return max(skip, take)

        return dp(len(jobs) - 1)