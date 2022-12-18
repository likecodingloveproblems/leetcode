package main

type LinkedList struct {
	Head *Node
	Tail *Node
	Size int
}

func NewLinkedList() LinkedList {
	return LinkedList{nil, nil, 0}
}

func (l *LinkedList) Prepend(item interface{}) {
	node := &Node{item, nil}
	if l.Head == nil {
		l.Head = node
		l.Tail = node
	} else {
		node.Next = l.Head
		l.Head = node
	}
	l.Size++
}

func (l *LinkedList) Append(item interface{}) {
	node := &Node{item, nil}
	if l.Head == nil {
		l.Head = node
		l.Tail = node
	} else {
		l.Tail.Next = node
		l.Tail = node
	}
	l.Size++
}

func (l *LinkedList) PopHead() *Node {
	if l.Size == 0 {
		panic("Linked List is empty!")
		return nil
	}
	head := l.Head
	l.Head = head.Next
	l.Size--
	return head
}

func (l *LinkedList) Pop() *Node {
	var tail *Node
	if l.Size == 0 {
		panic("Linked List is empty!")
		return nil
	}
	if l.Head == l.Tail {
		tail = l.Tail
		l.Tail = nil
		l.Head = nil
	} else {
		var newTail *Node
		node := l.Head
		for {
			if node.Next == l.Tail {
				newTail = node
				break
			} else {
				node = node.Next
			}
		}
		tail = l.Tail
		l.Tail = newTail
	}
	l.Size--
	return tail
}
