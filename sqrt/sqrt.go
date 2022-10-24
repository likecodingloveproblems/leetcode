package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	var pastZ float64
	eps := 1e-6
	z := x / 10
	for i := 0; i < 10; i++ {
		pastZ = z
		z -= (z*z - x) / (2 * z)
		fmt.Println(z)
		if math.Abs(z-pastZ) < eps {
			break
		}
	}
	return z
}

func main() {
	fmt.Println(math.Sqrt(2))
	fmt.Println(Sqrt(2))
}
