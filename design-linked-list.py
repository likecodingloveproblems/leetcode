class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

    def __str__(self) -> str:
        return str(self.val)


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get(self, index: int) -> int:
        if index >= self.count:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        if self.count == 0:
            self.head = node
            self.tail = node
        else:
            node.next, self.head = self.head, node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if self.count == 0:
            self.head, self.tail = node, node
        else:
            self.tail.next, self.tail = node, node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.count:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.count:
            self.addAtTail(val)
        else:
            new_node = ListNode(val)
            node = self.head
            for _ in range(index - 1):
                node = node.next
            new_node.next, node.next = node.next, new_node
            if node == self.tail:
                self.tail = new_node
        self.count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.count:
            return
        if index == 0:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head, self.tail = None, None
        else:
            node = self.head
            for _ in range(index - 1):
                node = node.next
            if node == self.tail:
                self.tail = node
            else:
                pass
            node.next = node.next.next
            if index == self.count - 1:
                self.tail = node.next
        self.count -= 1


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(0)
obj.addAtIndex(1, 4)
obj.addAtTail(8)
obj.addAtHead(5)
obj.addAtIndex(4, 3)
obj.addAtTail(0)
obj.addAtTail(5)
obj.addAtIndex(6, 3)
obj.deleteAtIndex(7)
obj.deleteAtIndex(5)
obj.addAtTail(4)
