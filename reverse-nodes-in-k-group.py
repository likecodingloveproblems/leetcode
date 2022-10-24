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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = head
        stack = list()
        while True:
            init_node = node
            for _ in range(k):
                if node == None:
                    break
                stack.append(node.val)
                node = node.next
            if len(stack) == k:
                for _ in range(k):
                    init_node.val = stack.pop()
                    init_node = init_node.next
            else:
                break
        return head


nodes, k = [1, 2, 3, 4, 5], 2
linked_list = LinkedList(nodes)
r = Solution().reverseKGroup(linked_list.head, k)
print(r)
