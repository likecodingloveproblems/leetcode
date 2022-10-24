class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __eq__(self, val) -> bool:
        return self.val == val

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self.next


class LinkedList:
    head: Node

    def __init__(self, items) -> None:
        self.head = Node(items[0])
        node = self.head
        for item in items[1:]:
            new_node = Node(item)
            new_node.prev = node
            node.next = new_node
            node = new_node
        node.next = self.head
        self.head.prev = node


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        linked_list = LinkedList(list(range(1, n + 1)))

        count = 1
        node = linked_list.head
        while node.next != node:
            if count % k == 0:
                node = node.delete()
                count = 1
            else:
                count += 1
                node = node.next
        return node.val


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(1, n + 1))
        step = k - 1
        index = step
        while len(l) > 1:
            l.pop(index)
            index += step
            if index >= len(l):
                index -= len(l)
                index %= len(l)
        return l.pop()


n, k = 5, 2
n, k = 6, 5
r = Solution().findTheWinner(n, k)
print(r)
