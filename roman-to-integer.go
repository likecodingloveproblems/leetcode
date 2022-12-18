package main

import "fmt"

func main() {
	s := "III"
	s = "LVIII"
	s = "MCMXCIV"
	fmt.Println(romanToInt(s))

}

func romanToInt(s string) int {
	var (
		result    int
		pastValue int
	)
	roman2Decimal := map[rune]int{
		'M': 1000,
		'D': 500,
		'C': 100,
		'L': 50,
		'X': 10,
		'V': 5,
		'I': 1,
	}
	for _, c := range s {
		if pastValue != 0 {
			if pastValue < roman2Decimal[c] {
				result = result + roman2Decimal[c] - pastValue
				pastValue = 0
			} else {
				result = result + pastValue
				pastValue = roman2Decimal[c]
			}
		} else {
			pastValue = roman2Decimal[c]
		}
	}
	result = result + pastValue
	return result
}
