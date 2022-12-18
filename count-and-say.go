package main

import (
	"fmt"
	"strconv"
)

func countAndSay(n int) string {
	if n < 1 {
		return ""
	}
	seq := "1"
	return _countAndSay(n, seq)
}

func _countAndSay(n int, seq string) string {
	var (
		char   rune
		count  int
		newSeq string
	)
	if n == 1 {
		return seq
	}
	n--
	for _, c := range seq {
		if c != char && char != rune(0) {
			newSeq += strconv.Itoa(count) + string(char)
			count = 0
		}
		count++
		char = c
	}
	if count != 0 {
		newSeq += strconv.Itoa(count) + string(char)
	}
	return _countAndSay(n, newSeq)
}

func main() {
	fmt.Println(countAndSay(4))
}
