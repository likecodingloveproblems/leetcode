from sortedcontainers import SortedList


class MinStack:
    def __init__(self):
        self.items = list()
        self.sorted_items = SortedList()

    def push(self, val: int) -> None:
        self.items.append(val)
        self.sorted_items.add(val)

    def pop(self) -> None:
        val = self.items.pop()
        self.sorted_items.remove(val)
        return val

    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.sorted_items[0]


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())  # return -3
print(minStack.pop())
print(minStack.top())  # return 0
print(minStack.getMin())  # return -2
