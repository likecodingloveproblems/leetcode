from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return str(self.val)

    def __str__(self) -> str:
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        first_node = head
        second_node = first_node.next
        next_node = second_node.next
        second_node.next = first_node
        first_node.next = next_node
        head = second_node
        self._swap_pairs(first_node)
        return head

    def _swap_pairs(self, prev_node):
        if prev_node.next is None or prev_node.next.next is None:
            return

        first_node = prev_node.next
        second_node = first_node.next
        next_node = second_node.next
        prev_node.next = second_node
        second_node.next = first_node
        first_node.next = next_node
        self._swap_pairs(first_node)


nodes = [1, 2, 3, 4, 5]
linked_list = LinkedList(nodes)
head = linked_list.head
r = Solution().swapPairs(head)
print(r)
