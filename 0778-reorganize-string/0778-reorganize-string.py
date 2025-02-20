class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxfreq = max(freq.values())
        if maxfreq > (len(s)+1)//2:
            return ""
        
        maxheap = [(-count,char) for char,count in freq.items() ]
        heapq.heapify(maxheap)
        prev_char, prev_count = "",0
        res = []
        while maxheap:
            count, char = heapq.heappop(maxheap)
            res.append(char)
            count += 1

            if prev_count < 0:
                heapq.heappush(maxheap,(prev_count,prev_char))
            
            prev_char,prev_count = char,count 

        return "".join(res)

