class MyQueue:

    def __init__(self):
        self.stack=[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        self.temp=[]
        while self.stack:
            self.temp.append(self.stack.pop())
        num=self.temp.pop()
        while self.temp:
            self.stack.append(self.temp.pop())
        return num

    def peek(self) -> int:
        self.temp=[]
        while self.stack:
            self.temp.append(self.stack.pop())
        num=self.temp.pop()
        self.stack.append(num)
        while self.temp:
            self.stack.append(self.temp.pop())
        return num

    def empty(self) -> bool:
        return True if len(self.stack)==0 else False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()