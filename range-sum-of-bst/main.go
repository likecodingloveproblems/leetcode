package main

import (
	"fmt"
)

func main() {
	root := &TreeNode{
		Val: 10,
		Left: &TreeNode{
			Val: 5,
			Left: &TreeNode{
				Val: 3,
			},
			Right: &TreeNode{
				Val: 7,
			},
		},
		Right: &TreeNode{
			Val: 15,
			Right: &TreeNode{
				Val: 18,
			},
		},
	}
	fmt.Println(rangeSumBST(root, 7, 15))
}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func getValIfIncluded(root *TreeNode, low, high int) int {
	if root.Val >= low && root.Val <= high {
		return root.Val
	}
	return 0
}

func goLeft(root *TreeNode, low int) bool {
	if root.Left != nil && root.Val >= low {
		return true
	}
	return false
}

func goRight(root *TreeNode, high int) bool {
	if root.Right != nil && root.Val <= high {
		return true
	}
	return false
}

func rangeSumBST(root *TreeNode, low int, high int) int {
	result := 0
	if goLeft(root, low) {
		result += rangeSumBST(root.Left, low, high)
	}
	if goRight(root, high) {
		result += rangeSumBST(root.Right, low, high)
	}
	result += getValIfIncluded(root, low, high)
	return result
}
