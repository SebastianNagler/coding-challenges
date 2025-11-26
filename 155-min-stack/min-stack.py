class MinStack:

    def __init__(self):
        self.array = []
        self.descending_mins = []
        

    def push(self, val: int) -> None:
        self.array.append(val)
        if (not self.descending_mins) or val <= self.descending_mins[-1]:
            self.descending_mins.append(val)
        
    def pop(self) -> None:
        val = self.array[-1]
        del self.array[-1]
        if val == self.descending_mins[-1]:
            del self.descending_mins[-1]
        return val
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.descending_mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()