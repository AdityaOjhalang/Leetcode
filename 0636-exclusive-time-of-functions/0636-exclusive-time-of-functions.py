class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        res = [0] * n
        stack = []
        prev_time = 0

        for log in logs:
            fid,typ,timestamp = log.split(":")
            fid = int(fid)
            timestamp = int(timestamp)
            if typ == "start":
                if stack:
                    res[stack[-1]] += timestamp - prev_time
                stack.append(fid)
                prev_time = timestamp
            else:
                func = stack.pop()
                res[func] += timestamp - prev_time + 1
                prev_time = timestamp + 1
        return res