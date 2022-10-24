from typing import Optional, List

from sortedcontainers import SortedList


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list = SortedList()
        indexes = set(range(len(lists)))
        while len(indexes) > 0:
            new_indexes = set()
            for index in indexes:
                node = lists[index]
                if node:
                    sorted_list.add(node.val)
                if node.next:
                    lists[index] = node.next
                    new_indexes.add(index)
            indexes = new_indexes

        if len(sorted_list) == 0:
            return
        head = ListNode(sorted_list[0])
        prev_node = head
        for val in sorted_list[1:]:
            node = ListNode(val)
            prev_node.next = node
            prev_node = node
        return head


nodes = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = list()
for node in nodes:
    lists.append(LinkedList(node).head)

r = Solution().mergeKLists(lists)
print(r)
