package main

import "fmt"

func convertToTitle(columnNumber int) string {
	var (
		A    = 'A'
		Z    = 'Z'
		char rune
	)
	char = (rune(columnNumber) - 1) / (Z - A)

	return string((columnNumber - 1) / (Z - A))

}

func main() {
	fmt.Println(convertToTitle(1))
}
