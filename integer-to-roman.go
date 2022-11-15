package main

import "fmt"

func main() {
	n := 1994
	fmt.Println(intToRoman(n))
}

func intToRoman(num int) string {
	var result string
	var roman string
	decimals := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	decimalToRoman := map[int]string{
		1000: "M",
		900:  "CM",
		500:  "D",
		400:  "CD",
		100:  "C",
		90:   "XC",
		50:   "L",
		40:   "XL",
		10:   "X",
		9:    "IX",
		5:    "V",
		4:    "IV",
		1:    "I",
	}

	for _, decimal := range decimals {
		roman = decimalToRoman[decimal]
		if count := num / decimal; count > 0 {
			for i := 0; i < count; i++ {
				result = result + roman
			}
			num = num - count*decimal
		}

	}
	return result
}
