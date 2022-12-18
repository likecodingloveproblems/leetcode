package main

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return int(_minDepth(root, 1))
}

func _minDepth(root *TreeNode, count int) int {
	if root.Left == nil && root.Right == nil {
		return count
	}
	count++
	if root.Left == nil {
		return _minDepth(root.Right, count)
	} else if root.Right == nil {
		return _minDepth(root.Left, count)
	} else {
		leftDepth := _minDepth(root.Left, count)
		rightDepth := _minDepth(root.Right, count)
		if leftDepth > rightDepth {
			return rightDepth
		} else {
			return leftDepth
		}
	}
}
