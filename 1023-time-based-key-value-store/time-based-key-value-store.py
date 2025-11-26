class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.map) or timestamp < self.map[key][0][0]:
            return ''
        left = 0
        right = len(self.map[key]) - 1
        while left <= right:
            mid = (left + right) // 2
            time = self.map[key][mid][0]
            if time == timestamp:
                return self.map[key][mid][1]
            elif time < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        return self.map[key][left-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)