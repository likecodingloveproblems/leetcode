# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def linked_list_generator(nums, cycle):
    node = None
    for i in range(len(nums) - 1, -1, -1):
        if node:
            new_node = ListNode(nums[i])
            new_node.next = node
            node = new_node
        else:
            node = ListNode(nums[i])
        if i == len(nums) - 1:
            tail = node
        if i == cycle:
            tail.next = node
        if i == 0:
            head = node

    return head


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = set()
        index = 0
        while True:
            if head in nodes:
                return head
            else:
                nodes.add(head)
                index += 1

            if head and head.next:
                head = head.next
            else:
                return None


nums, cycle = [3, 2, 0, -4], 1
head = linked_list_generator(nums, cycle)
r = Solution().detectCycle(head)
print(r)
