# Definition for singly-linked list.
from typing import List, Optional
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        new_node = None
        while node != None:
            new_node = ListNode(node.val, new_node)
            node = node.next
        return new_node


head = [1, 2, 3, 4, 5]


def list_to_linked_list(l: List):
    if len(l) == 0:
        return
    root = ListNode(l[0])
    node = root
    for item in l[1:]:
        new_node = ListNode(item)
        node.next = new_node
        node = new_node
    return root


head = list_to_linked_list(head)
s = Solution().reverseList(head)
print(s)
