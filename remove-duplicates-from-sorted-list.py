# Definition for singly-linked list.
from termios import VLNEXT
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val)

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev_node = node = head
        values = set()
        while node != None:
            if node.val in values:
                prev_node.next = node = node.next
            else:
                values.add(node.val)
                prev_node = node
                node = node.next

        return head


head = [1, 1, 2, 3, 3]


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
s = Solution().deleteDuplicates(head)
print(s)
