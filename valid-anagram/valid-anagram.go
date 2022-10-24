package main

import "fmt"

func isAnagram(s string, t string) bool {
	stringToMap := func(s string) map[rune]int {
		charMap := map[rune]int{}
		for _, char := range s {
			if v, exists := charMap[char]; exists {
				charMap[char] = v + 1
			} else {
				charMap[char] = 1
			}
		}
		return charMap
	}
	sMap := stringToMap(s)
	tMap := stringToMap(t)
	for sk, sv := range sMap {
		if tv, _ := tMap[sk]; tv != sv {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isAnagram("anagram", "nagaram"))
}
