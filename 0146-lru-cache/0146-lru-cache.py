class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.left,self.right = Node(0,0),Node(0,0)
        self.cache = {}
        self.left.next ,self.right.prev = self.right,self.left

    def remove(self,node):
        prev,nxt = node.prev,node.next
        prev.next, nxt.prev = nxt,prev

    
    def insert(self,node):
        prev,nxt = self.right.prev,self.right
        node.prev,node.next = prev,nxt
        prev.next = nxt.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instaantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)