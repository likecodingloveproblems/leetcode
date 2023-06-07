package main

import (
	"fmt"
)

func minPartitions(n string) int {
	var max int
	for _, digit := range n {
		digit_value := int(digit - '0')
		if digit_value > max {
			max = digit_value
		}
	}
	return max
}

func main() {
	n := "231"
	fmt.Println(minPartitions(n))
}
