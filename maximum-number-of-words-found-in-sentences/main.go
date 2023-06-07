package main

import (
	"fmt"
)

func mostWordsFound(sentences []string) int {
	var maxWord int
	for _, sentence := range sentences {
		count := wordCount(sentence)
		if count > maxWord {
			maxWord = count
		}
	}
	return maxWord
}

func wordCount(sentence string) int {
	var spaceCount int
	for _, char := range sentence {
		if char == ' ' {
			spaceCount++
		}
	}
	return spaceCount + 1
}

func main() {
	sentences := []string{"alice and bob love leetcode", "i think so too", "this is great thanks very much"}
	sentences = []string{"please wait", "continue to fight", "continue to win"}
	fmt.Println(mostWordsFound(sentences))
}
