from collections import deque
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)


class LinkedList:
    head: ListNode

    def __init__(self, items) -> None:
        self.head = ListNode(items[0])
        node = self.head
        for item in items[1:]:
            new_node = ListNode(item)
            node.next = new_node
            node = new_node


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        nodes = deque()
        while node != None:
            nodes.append(node.val)
            node = node.next
        node = head
        while len(nodes):
            node.val = nodes.popleft()
            node = node.next
            if len(nodes):
                node.val = nodes.pop()
                node = node.next


nodes = [1, 2, 3, 4, 5]
linked_list = LinkedList(nodes)
Solution().reorderList(linked_list.head)
print(linked_list.head)
