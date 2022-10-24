from re import I
from typing import List
import numpy as np


class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __eq__(self, val) -> bool:
        return self.val == val


class LinkedList:
    head: Node

    def __init__(self, items) -> None:
        self.head = Node(items[0])
        node = self.head
        for item in items[1:]:
            new_node = Node(item)
            new_node.prev = node
            node.next = new_node
            node = new_node
        node.next = self.head
        self.head.prev = node


class Solution:
    directions = LinkedList(["r", "d", "l", "u"])

    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = self.directions.head
        num = 1
        count = 0
        margin = 0
        row_index, col_index = n - 1, 0
        mat = np.zeros((n, n), int)
        while num <= n**2:
            if direction == "r":
                row_index, col_index = margin, margin + count
            elif direction == "d":
                row_index, col_index = margin + count, n - margin - 1
            elif direction == "l":
                row_index, col_index = n - margin - 1, n - margin - 1 - count
            elif direction == "u":
                row_index, col_index = n - margin - 1 - count, margin
            mat[row_index][col_index] = num

            count += 1
            num += 1
            if count == n - 1 - 2 * margin:
                if direction == "u":
                    margin += 1
                direction = direction.next
                count = 0
        return mat.tolist()


n = 5
r = Solution().generateMatrix(n)
print(r)
