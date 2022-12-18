from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class GenerateTree:
    def generate_tree(self, values):
        return self._generate_depth_nodes(values, 0)

    def _generate_depth_nodes(self, values, current_index, nodes=None):
        if current_index >= len(values):
            return
        if nodes is None:
            head = TreeNode(values[current_index])
            new_nodes = [head]
            current_index += 1
        else:
            new_nodes = list()
            for node in nodes:
                if isinstance(values[current_index], int):
                    node.left = TreeNode(values[current_index])
                    new_nodes.append(node.left)
                current_index += 1
                if isinstance(values[current_index], int):
                    node.right = TreeNode(values[current_index])
                    new_nodes.append(node.right)
                current_index += 1

        self._generate_depth_nodes(values, current_index, new_nodes)
        if current_index == 1:
            return head


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.vals = iter(self._next(self.root))
        self.next_val = None

    def next(self) -> int:
        if self.next_val is not None:
            temp = self.next_val
            self.next_val = None
            return temp
        else:
            try:
                return next(self.vals)
            except StopIteration:
                return

    def _next(self, node):
        if node.left is None and node.right is None:
            yield node.val
        else:
            if node.left:
                yield from self._next(node.left)
            yield node.val
            if node.right:
                yield from self._next(node.right)

    def hasNext(self) -> bool:
        if self.next_val:
            return True
        try:
            self.next_val = next(self.vals)
            return True
        except StopIteration:
            return False


nodes = [
    41,
    37,
    44,
    24,
    39,
    42,
    48,
    1,
    35,
    38,
    40,
    None,
    43,
    46,
    49,
    0,
    2,
    30,
    36,
    None,
    None,
    None,
    None,
    None,
    None,
    45,
    47,
    None,
    None,
    None,
    None,
    None,
    4,
    29,
    32,
    None,
    None,
    None,
    None,
    None,
    None,
    3,
    9,
    26,
    None,
    31,
    34,
    None,
    None,
    7,
    11,
    25,
    27,
    None,
    None,
    33,
    None,
    6,
    8,
    10,
    16,
    None,
    None,
    None,
    28,
    None,
    None,
    5,
    None,
    None,
    None,
    None,
    None,
    15,
    19,
    None,
    None,
    None,
    None,
    12,
    None,
    18,
    20,
    None,
    13,
    17,
    None,
    None,
    22,
    None,
    14,
    None,
    None,
    21,
    23,
]

root = GenerateTree().generate_tree(nodes)
obj = BSTIterator(root)
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
