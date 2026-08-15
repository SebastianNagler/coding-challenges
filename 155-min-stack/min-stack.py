class MinStack:

    def __init__(self):
        self.stack = []
        self.min_arr = [float("inf")]
        
    def push(self, value: int) -> None:
        self.stack.append(value)
        if value <= self.min_arr[-1]:
            self.min_arr.append(value)

    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val == self.min_arr[-1]:
            self.min_arr.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_arr[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()