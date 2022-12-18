package main

import (
	"fmt"
	"math"
)

func mySqrt(x int) int {
	if x < 2 {
		return x
	}
	var (
		xFloat           = float64(x)
		first, last, mid = 0.0, xFloat, xFloat / 2
		tol              = 0.01
		err              = xFloat - mid*mid
	)
	for math.Abs(err) > tol {
		if err > 0 {
			first = mid
		} else {
			last = mid
		}
		mid = (first + last) / 2
		err = xFloat - mid*mid
	}
	return int(mid)
}

func main() {
	x := 1
	fmt.Println(mySqrt(x))
}
