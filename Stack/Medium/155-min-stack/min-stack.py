class MinStack:
    # Complexity of all is O(1) per the problem statement
    # Space Complexity O(n)

    def __init__(self):
        self.stack = []
        self.min = None
        self.prev = []
        

    def push(self, val: int) -> None:
        if self.stack == []: self.min = val
        elif self.min >= val:
            self.prev.append(self.min)
            self.min = val
        self.stack.append(val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            print(val, self.prev)
            if self.stack == []: 
                self.min = None
            else: 
                self.min = self.prev.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()