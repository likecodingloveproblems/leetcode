package main

import (
	"fmt"

	"github.com/golang-collections/collections/stack"
)

func Xor(a, b, c bool) bool {
	return (a != b) != c
}

func AndOr(a, b, c bool) bool {
	return (a && b) || (a && c) || (b && c)
}

func getByte(s string, i int) bool {
	lastIndex := len(s) - 1
	i = lastIndex - i
	if i < 0 || s[i] == '0' {
		return false
	} else {
		return true
	}
}

func boolToRune(b bool) rune {
	if b {
		return '1'
	} else {
		return '0'
	}
}

func addBinary(a string, b string) string {
	var (
		aByte    bool
		bByte    bool
		overhead bool
		sumStack = stack.New()
		sum      = []rune{}
	)
	for i := 0; i < len(a) || i < len(b); i++ {
		aByte = getByte(a, i)
		bByte = getByte(b, i)
		sumStack.Push(Xor(aByte, bByte, overhead))
		overhead = AndOr(aByte, bByte, overhead)
	}
	if overhead {
		sumStack.Push(overhead)
	}
	for sumStack.Len() > 0 {
		sum = append(sum, boolToRune(sumStack.Pop().(bool)))
	}
	return string(sum)
}

func main() {
	a := "1011"
	b := "1010"
	c := addBinary(a, b)
	fmt.Println(c)
}
