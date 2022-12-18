package main

import (
	"fmt"
)

func toIndex(char rune) int {
	return 0
}

type set struct {
	items []bool
}

func (s *set) add(char rune) {
	index := toIndex(char)
	s.items[index] = false
}

func isUnique(s string) bool {
	chars := map[rune]bool{}
	for _, char := range s {
		if _, e := chars[char]; e {
			return false
		} else {
			chars[char] = false
		}
	}
	return true
}

func main() {
	s := "ali"
	fmt.Println(isUnique(s))
}
