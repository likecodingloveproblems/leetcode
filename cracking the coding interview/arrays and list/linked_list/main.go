package main

import "fmt"

func main() {
	l := NewLinkedList()
	l.Append(2)
	l.Append("ali")
	fmt.Println(l.PopHead().Next.Item == "ali")
}
