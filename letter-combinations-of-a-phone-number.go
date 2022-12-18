package main

import (
	"fmt"
	"strconv"
)

func main() {
	digits := "123456789195561"
	result := letterCombinations(digits)
	fmt.Println(len(result))
}

var numToLetter = map[int][]rune{
	2: {'a', 'b', 'c'},
	3: {'d', 'e', 'f'},
	4: {'g', 'h', 'i'},
	5: {'j', 'k', 'l'},
	6: {'m', 'n', 'o'},
	7: {'p', 'q', 'r', 's'},
	8: {'t', 'u', 'v'},
	9: {'w', 'x', 'y', 'z'},
}

func letterCombinations(digits string) []string {
	result := []string{}
	chars := [][]rune{}
	var char []rune
	for _, c := range digits {
		num, _ := strconv.Atoi(string(c))
		if c, e := numToLetter[num]; e {
			chars = append(chars, c)
		}
	}
	positions := make([]int, len(chars))
	for {
		char = []rune{}
		for i, pos := range positions {
			char = append(char, chars[i][pos])
		}
		result = append(result, string(char))
		for i := len(chars) - 1; i >= 0; i-- {
			positions[i]++
			if positions[i] == len(chars[i]) {
				positions[i] = 0
				if i == 0 {
					return result
				} else {
					continue
				}
			} else {
				break
			}
		}
	}
}
