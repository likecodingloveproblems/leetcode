package main

import "fmt"

func firstUniqueCharacter(s string) int {
	charMap := map[rune]int{}
	for _, char := range s {
		if v, exists := charMap[char]; exists {
			charMap[char] = v + 1
		} else {
			charMap[char] = 1
		}
	}

	for index, char := range s {
		if v, _ := charMap[char]; v == 1 {
			return index
		}
	}
	return -1
}

func main() {
	s := "leetcode"
	r := firstUniqueCharacter(s)
	fmt.Println(r)
}
