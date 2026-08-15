class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = deque()
        self.map = {}

    def get(self, key: int) -> int:
        if key in self.map:
            val = self.map[key]
            del self.map[key]
            self.map[key] = val
            return val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if len(self.map) == self.capacity and key not in self.map:
            del self.map[next(iter(self.map))]
        if key in self.map:
            del self.map[key]
        self.map[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)