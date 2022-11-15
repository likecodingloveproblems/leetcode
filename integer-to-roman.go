package main

import "fmt"

func main() {
	n := 1994
	fmt.Println(intToRoman(n))
}

func intToRoman(num int) string {
	var result string
	decimalKeys := []int{1000, 500, 100, 50, 10, 5, 1}
	decimalToRoman := map[int]string{
		1000: "M",
		500:  "D",
		100:  "C",
		50:   "L",
		10:   "X",
		5:    "V",
		1:    "I",
	}
	combKeys := []int{900, 400, 90, 40, 9, 4}
	combinationMap := map[int]string{
		900: "CM",
		400: "CD",
		90:  "XC",
		40:  "XL",
		9:   "IX",
		4:   "IV",
	}

	for i, decimal := range decimalKeys {
		if num/decimal > 0 {
			for i := 0; i < num/decimal; i++ {
				result = result + decimalToRoman[decimal]
			}
			num = num - (num/decimal)*decimal
		}
		if i < len(combKeys) && num/combKeys[i] == 1 {
			result = result + combinationMap[combKeys[i]]
			num = num - (num/combKeys[i])*combKeys[i]
		}
	}
	return result
}
