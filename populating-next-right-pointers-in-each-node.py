class TreeNode:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

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
                if current_index < len(values) and values[current_index]:
                    node.left = TreeNode(values[current_index])
                    new_nodes.append(node.left)
                current_index += 1
                if current_index < len(values) and values[current_index]:
                    node.right = TreeNode(values[current_index])
                    new_nodes.append(node.right)
                current_index += 1

        self._generate_depth_nodes(values, current_index, new_nodes)
        if current_index == 1:
            return head


class Solution:
    def connect(self, nodes):
        child_nodes = list()
        if isinstance(nodes, TreeNode):
            nodes = [nodes]
        if len(nodes) == 0:
            return
        for i, node in enumerate(nodes):
            if node.left:
                child_nodes.append(node.left)
            if node.right:
                child_nodes.append(node.right)
            i += 1
            if i < len(nodes):
                node.next = nodes[i]
        self.connect(child_nodes)

        return nodes[0]


nodes = [1, 2, 3, 4, 5, 6, 7]
head = GenerateTree().generate_tree(nodes)
r = Solution().connect(head)
print(r)
