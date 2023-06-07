package main

import (
	"fmt"
	"strings"
)

func interpret(command string) string {
	return strings.ReplaceAll(
		strings.ReplaceAll(command, "()", "o"),
		"(al)", "al")
}

func main() {
	command := "G()()()()(al)"
	fmt.Println(interpret(command))
}
