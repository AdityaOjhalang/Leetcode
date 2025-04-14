class SmallestInfiniteSet:

    def __init__(self):
        self.hset = set()
        self.heap = []
        self.curr = 1

    def popSmallest(self) -> int:
        if self.heap:
            small = heapq.heappop(self.heap)
            self.hset.remove(small)
        else:
            small = self.curr
            self.curr += 1
        return small       

    def addBack(self, num: int) -> None:
        if num < self.curr and num not in self.hset:
            self.hset.add(num)
            heapq.heappush(self.heap,num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)