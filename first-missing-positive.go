package main

import "fmt"

func firstMissingPositive(nums []int) int {
	var (
		max     int
		missing int
	)
	set := map[int]bool{}
	for _, num := range nums {
		if num > max {
			max = num
		}
		set[num] = false
	}
	for i := 1; i <= max; i++ {
		if _, e := set[i]; !e {
			missing = i
			break
		}
	}
	if missing == 0 {
		return max + 1
	} else {
		return missing
	}
}

func main() {
	fmt.Println(firstMissingPositive([]int{3, 2, 0}))
}
