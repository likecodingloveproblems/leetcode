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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        node = head
        while node != None:
            if node.next and node.next.val == node.val:
                node = self.getNode(node, node.val)
                if prev_node:
                    prev_node.next = node
                else:
                    head = node
            else:
                prev_node = node
                node = node.next
        return head

    def getNode(self, node, val):
        if node.val == val:
            return self.getNode(node.next, val)
        else:
            return node


nodes = [1, 2, 3, 3, 4, 4, 5]
nodes = [1, 1, 1, 2, 3]
linked_list = LinkedList(nodes)
head = linked_list.head
r = Solution().deleteDuplicates(head)
print(r)
