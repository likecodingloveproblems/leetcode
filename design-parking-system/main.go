package main

import (
	"fmt"
)

type ParkingSystem struct {
	size []int
}

func Constructor(big int, medium int, small int) ParkingSystem {
	return ParkingSystem{size: []int{big, medium, small}}
}

func (this *ParkingSystem) AddCar(carType int) bool {
	carType--
	if this.size[carType] > 0 {
		this.size[carType]--
		return true
	} else {
		return false
	}
}

func main() {
	parking := Constructor(1, 1, 0)
	for _, car := range []int{1, 2, 3, 1} {
		fmt.Println(parking.AddCar(car))
	}
}
