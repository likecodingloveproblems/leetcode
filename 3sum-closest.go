package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	nums := []int{-1, 2, 1, -4}
	target := 1
	fmt.Println(threeSumClosest(nums, target))
}

func threeSumClosest(nums []int, target int) int {
	var sum int
	var closestSum int = 1000000000000000000
	sort.Ints(nums)
	for i := range nums[:len(nums)-2] {
		sum = 0
		firstIndex := i + 1
		lastIndex := len(nums) - 1
		for firstIndex < lastIndex {
			sum = nums[i] + nums[firstIndex] + nums[lastIndex]
			if math.Abs(float64(closestSum-target)) > math.Abs(float64(sum-target)) {
				closestSum = sum
			}
			if sum < target {
				firstIndex++
			} else {
				lastIndex--
			}
		}
	}
	return closestSum
}
