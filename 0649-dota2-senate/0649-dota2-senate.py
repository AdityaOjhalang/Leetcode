class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rq,dq = deque(), deque()
        n = len(senate) + 1
        for i,char in enumerate(senate):
            if char == "R":
                rq.append(i)
            if char == "D":
                dq.append(i)
        while rq and dq:
            r = rq.popleft()
            d = dq.popleft()
            if r < d:
                rq.append(r + n)
            else:
                dq.append(d + n)
        return "Radiant" if rq else "Dire"