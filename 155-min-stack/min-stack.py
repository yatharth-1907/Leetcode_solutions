class MinStack:

    def __init__(self):
        self.minimum=float('inf')
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val<self.minimum:
            self.minimum=val

    def pop(self) -> None:
        self.stack.pop()
        self.minimum=float('inf')
        for i in self.stack:
            if i<self.minimum:
                self.minimum=i

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()