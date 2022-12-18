package main

import (
	"fmt"
	"unicode"
)

func IsLetterOrNumber(c rune) bool {
	if (c < 'a' || c > 'z') && (c < 'A' || c > 'Z') && (c < '0' || c > '9') {
		return false
	} else {
		return true
	}
}

func isPalindrome(s string) bool {
	letters := []rune{}
	for _, c := range s {
		if IsLetterOrNumber(c) {
			letters = append(letters, unicode.ToLower(c))
		}
	}
	for first, last := 0, len(letters)-1; first < last; first, last = first+1, last-1 {
		if letters[first] != letters[last] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isPalindrome("0P"))
}
