class Solution:
    def reorganizeString(self, s: str) -> str:
        hmap = Counter(s)
        maxfreq = max(hmap.values())
        if maxfreq > (len(s) + 1)//2:
            return ""
        
        minheap = [(-count,val) for (val,count) in hmap.items()]
        heapq.heapify(minheap) 

        prev_char,prev_count = None,0
        res = []
        while minheap:
            count,val = heapq.heappop(minheap)
            count += 1
            res.append(val)

            if prev_count < 0:
                heapq.heappush(minheap,(prev_count,prev_char))

            prev_count,prev_char = count, val

        return "".join(res)
