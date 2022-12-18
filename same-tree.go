package main

func main() {

}

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func generateTree(values []int) (root *TreeNode) {
	root = &TreeNode{values[0], nil, nil}
	for 
	return
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}
	return (
		p != nil && q != nil &&
		p.Val == q.Val &&
	 	isSameTree(p.Left, q.Left) &&
		isSameTree(p.Right, q.Right))
}
