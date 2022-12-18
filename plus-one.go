package main

import "fmt"

func plusOne(digits []int) []int {
	i := len(digits) - 1
	for i >= 0 {
		digits[i]++
		if digits[i] == 10 {
			digits[i] = 0
			i--
		} else {
			break
		}
	}
	if i < 0 {
		// prepend 1 to digits
		digits = append(digits, 0)
		copy(digits, digits[1:])
		digits[0] = 1
	}
	return digits
}

func main() {
	digits := []int{9, 9, 9}
	digits = plusOne(digits)
	fmt.Println(digits)
}
