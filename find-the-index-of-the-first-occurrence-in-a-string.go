package main

import (
	"fmt"
)

func strStr(haystack string, needle string) int {
	match := false
	for hIndex := range haystack {
		for nIndex := range needle {
			if hIndex+nIndex >= len(haystack) || haystack[hIndex+nIndex] != needle[nIndex] {
				match = false
				break
			} else {
				match = true
			}
		}
		if match {
			return hIndex
		}
	}
	return -1
}

func main() {
	haystack := "sadbutsad"
	needle := "dbus"
	fmt.Println(strStr(haystack, needle))
}
