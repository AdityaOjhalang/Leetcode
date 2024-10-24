class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:

        neighbors = defaultdict(list)

        for i in range(len(equations)):
            x, y = equations[i]
            val = values[i]
            neighbors[x].append((y, val))
            neighbors[y].append((x, 1/val))


        def querycalc(start, end):
            if start not in neighbors or end not in neighbors:
                return -1

            seen = {start}
            queue = deque([(start, 1)])

            while queue:
                node, ratio = queue.popleft()
                if node == end:
                    return ratio

                for neigh,weight in neighbors[node]:
                    if neigh not in seen:
                        seen.add(neigh)
                        queue.append((neigh, ratio * weight))
            return -1

        ans = []
        for i, val in enumerate(queries):
            n, d = val
            ans.append(querycalc(n, d))
        return ans
