# Definition for singly-linked list.
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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        prev_node = None
        node = head
        while node:
            if node.val == val:
                if node == head:
                    head = head.next
                else:
                    prev_node.next = node.next
                    node = prev_node.next
                    continue
            prev_node = node
            node = node.next

        return head


head = [1, 2, 2, 1]
val = 2


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
s = Solution().removeElements(head, val)
print(s)
