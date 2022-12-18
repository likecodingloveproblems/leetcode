package main

type Node struct {
	Item interface{}
	Next *Node
}

func (n *Node) PushNext(node *Node) {
	nextNode := n.Next
	n.Next = node
	node.Next = nextNode
}

type Person struct {
	Name string
}
