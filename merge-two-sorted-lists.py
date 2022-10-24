# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        root = node = None
        while list1 or list2:
            new_node = ListNode()
            val1 = list1.val if list1 else None
            val2 = list2.val if list2 else None
            if val2 is not None and (val1 is None or val1 > val2):
                new_node.val = val2
                list2 = list2.next
            else:
                new_node.val = val1
                list1 = list1.next
            if node:
                node.next = new_node
                node = new_node
            else:
                root = node = new_node

        return root


list1 = [1, 2, 4]
list2 = [1, 3, 4]
list1 = []
list2 = [0]


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


list1 = list_to_linked_list(list1)
list2 = list_to_linked_list(list2)
s = Solution().mergeTwoLists(list1, list2)
print(s)
