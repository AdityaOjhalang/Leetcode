class RandomizedSet:

    def __init__(self):
        self.hmap = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        if val in self.hmap:
            return False
        self.list.append(val)
        self.hmap[val] = len(self.list) - 1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.hmap:
            last,i = self.list[-1] , self.hmap[val]
            self.list[i] = last
            self.hmap[last] = i
            self.list.pop()
            del self.hmap[val]   
            return True
        else:
            return False    

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()