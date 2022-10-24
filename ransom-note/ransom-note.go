package main

import "fmt"

func canConstruct(ransomNote string, magazine string) bool {
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
	magazineMap := stringToMap(magazine)
	ransomNoteMap := stringToMap(ransomNote)
	for _, char := range ransomNote {
		magazineValue, _ := magazineMap[char]
		ransomNoteValue, _ := ransomNoteMap[char]
		if ransomNoteValue > magazineValue {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(canConstruct("aab", "caba"))
}
