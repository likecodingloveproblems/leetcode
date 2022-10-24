class MyQueue:
    def __init__(self):
        self.stack = list()
        self.stack2 = list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        length = len(self.stack)
        for _ in range(length):
            self.stack2.append(self.stack.pop())
        result = self.stack2.pop()
        for _ in range(length - 1):
            self.stack.append(self.stack2.pop())
        return result

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return not bool(len(self.stack))


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
param_1 = obj.peek()
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
print(param_1, param_2, param_3, param_4)
