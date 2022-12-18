package main

import "fmt"

func main() {
	strs := []string{"flower", "flow", "flight"}
	fmt.Println(longestCommonPrefix(strs))
}

func longestCommonPrefix(strs []string) string {
	prefix := []byte(strs[0])
	newPrefix := []byte{}
	for _, str := range strs[1:] {
		for i := range prefix {
			if i < len(str) && prefix[i] == str[i] {
				newPrefix = append(newPrefix, prefix[i])
			} else {
				break
			}
		}
		prefix = newPrefix
		newPrefix = []byte{}
	}
	return string(prefix)
}
